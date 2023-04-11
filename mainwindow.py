from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt6.QtCore import QMargins, QTimer
from PyQt6.QtGui import QPixmap
from menu_frame import Menu
from camera_frame import CameraFrame
from dashboard_frame import DashboardFrame
from login_frame import LoginFrame
from data_parse import DataParser
import sys

class mainwindow(QWidget):
    """
    This is the main window of the application.
    All functions reside within this class.
    """
    def __init__(self):
        super(mainwindow, self).__init__()
        self.lastSize = self.size()
        self.data = DataParser()
        self.initUI()
        self.createLayout()
        self.addPages()
        self.dashboardActive()
        #self.refreshData()
        #self.setTimer()
        self.connectMenuButtons()
        self.connectCameraSliders()
        self.connectPrimaireBediening()
        self.changeStoplichtState()
        self.show()   

    def initUI(self):
        self.setGeometry(300, 100, 1500, 800)      

    def createLayout(self):
        self.mainwindow_layout = QGridLayout()
        self.mainwindow_layout.setSpacing(0)
        self.mainwindow_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.setLayout(self.mainwindow_layout)

    def addPages(self):
        self.menu = Menu(self)
        self.camera_window = CameraFrame()
        self.login_window = LoginFrame(self)
        self.dashboard_window = DashboardFrame(self)
        
        self.mainwindow_layout.addWidget(self.menu, 0, 0)
        self.mainwindow_layout.addWidget(self.camera_window, 0, 1)
        self.mainwindow_layout.addWidget(self.dashboard_window, 0, 1)
        self.mainwindow_layout.addWidget(self.login_window, 0, 1)

    def connectMenuButtons(self):
        self.menu.button_dashboard.clicked.connect(self.dashboardActive)
        self.menu.button_camera.clicked.connect(self.cameraActive)
        self.menu.button_logout.clicked.connect(self.loginActive)

    def loginActive(self):
        self.login_window.show()
        self.menu.button_dashboard.contentActive(False)
        self.menu.button_camera.contentActive(False)
        self.dashboard_window.hide()
        self.menu.hide()
        self.camera_window.hide()

    def dashboardActive(self):
        self.menu.button_dashboard.contentActive(True)
        self.menu.button_camera.contentActive(False)
        self.dashboard_window.show()
        self.camera_window.hide()
        self.login_window.hide()

    def cameraActive(self):
        self.menu.button_dashboard.contentActive(False)
        self.menu.button_camera.contentActive(True)
        self.dashboard_window.hide()
        self.camera_window.show()

    def setTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshData)
        self.timer.start(1000) 

    def refreshData(self):
        # VERLICHTING 
        # {id, level, capacity, energy_usage, light_hours}
        verlichting = self.data.lighting_state
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.niveau.setWaarde(verlichting[0]['level']) 
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.capaciteit.setWaarde(verlichting[1]['capacity'])
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.energieverbruik.setWaarde(verlichting[2]['energy_usage'])
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.branduren.setWaarde(verlichting[3]['light_hours'])
        
        # CCTV
        # {id, pan, tilt, zoom, preset}
        cctv = self.data.cctv_state
        self.camera_window.controlpanel.panel_camera1.option_slider_pan.setValue(cctv[0]['pan'])
        self.camera_window.controlpanel.panel_camera1.option_slider_tilt.setValue(cctv[0]['tilt'])
        self.camera_window.controlpanel.panel_camera1.option_slider_zoom.setValue(cctv[0]['zoom'])
        self.camera_window.controlpanel.panel_camera1.option_slider_preset.setValue(cctv[0]['preset'])
       
        # VRI 
        # {id, available_state, error_state, state}
        vri = self.data.vri_state
        self.dashboard_window.systemen_detecties.rijbaan1.verkeerslicht_details.state.setWaarde(vri[0]['state'])
        self.dashboard_window.systemen_detecties.rijbaan1.verkeerslicht_details.beschikbaarheid.setWaarde(vri[0]['available_state'])
        self.dashboard_window.systemen_detecties.rijbaan1.verkeerslicht_details.error.setWaarde(vri[0]['error_state'])
       
        # BARRIER 
        # {id, state, available_state, movement_state, obstacle_state, error_state}
        barrier = self.data.barrier_state
        status_barrier = barrier[0]['state']
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.state.setWaarde(barrier[0]['state'])
        if status_barrier == "up":
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Open")
        else:
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Dicht")
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.beschikbaarheid.setWaarde(barrier[1]['available_state'])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.movement.setWaarde(barrier[0]['movement_state'])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.obstacle.setWaarde(barrier[0]['obstacle_state'])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.error.setWaarde(barrier[0]['error_state'])

        # MATRIX 
        # {id, state, available_state, flashing_state, error_state}
        matrix = self.data.msi_state
        self.dashboard_window.overzichts_plattegrond.matrix1.matrixbord.setStatus(matrix[0]['state'])
 
        #SENSOR
        #sensor = self.data.sensor_state
        #self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.CO.setWaarde(barrier[0])
        #self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.CO2.setWaarde(barrier[1])
        #self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.NO2.setWaarde(barrier[2])

    def connectCameraSliders(self):
        self.camera_window.controlpanel.panel_camera1.option_slider_pan.valueChanged.connect(self.changePan)
        self.camera_window.controlpanel.panel_camera1.option_slider_tilt.valueChanged.connect(self.changeTilt)
        self.camera_window.controlpanel.panel_camera1.option_slider_zoom.valueChanged.connect(self.changeZoom)
        self.camera_window.controlpanel.panel_camera1.option_slider_preset.valueChanged.connect(self.changePreset)

    def changePan(self):
        print(self.camera_window.controlpanel.panel_camera1.option_slider_pan.value())
        #self.data.Control_CCTV(0,'change_pan',self.camera_window.controlpanel.panel_camera1.option_slider_pan.value())

    def changeTilt(self):
        print(self.camera_window.controlpanel.panel_camera1.option_slider_tilt.value())
        #self.data.Control_CCTV(0,'change_tilt',self.camera_window.controlpanel.panel_camera1.option_slider_tilt.value())

    def changeZoom(self):
        print(self.camera_window.controlpanel.panel_camera1.option_slider_zoom.value())
        #self.data.Control_CCTV(0,'change_zoom',self.camera_window.controlpanel.panel_camera1.option_slider_zoom.value())

    def changePreset(self):
        print(self.camera_window.controlpanel.panel_camera1.option_slider_preset.value())
        #self.data.Control_CCTV(0,'change_preset',self.camera_window.controlpanel.panel_camera1.option_slider_preset.value())

    def connectPrimaireBediening(self):
        self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.clicked.connect(self.openSlagboom)
        self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.clicked.connect(self.closeSlagboom)
        self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.noodstop.clicked.connect(self.noodStop)
        self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.rijbaan_status.currentIndexChanged.connect(self.changeTunnelState)
        self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.stoplicht.currentIndexChanged.connect(self.changeStoplichtState)

    def noodStop(self):
        pass

    def openSlagboom(self):
        if self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.isChecked() == False:
            slagboomBarrier = self.data.barrier_state
            if slagboomBarrier[0] == "up":
                self.data.Control_Barrier(0,'up')
                self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(False)
                self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(True)
        else:
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setChecked(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(True)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Open")

    def closeSlagboom(self):
        if self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.isChecked() == False:
            slagboomBarrier = self.data.barrier_state
            if slagboomBarrier[0] == "down":
                self.data.Control_Barrier(0,'down')
                self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Dicht")
                self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(False)
                self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(True)
        else:
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setChecked(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Dicht")  
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(True)     

    def changeTunnelState(self):
        index = self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.rijbaan_status.currentIndex()
        print(index)

    def changeStoplichtState(self):
        index = self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.stoplicht.currentIndex()
        self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.changeStoplichtStatus(index)
        print(index)
        
if __name__ == '__main__':
    app = QApplication([])
    mw = mainwindow()
    mw.move
    sys.exit(app.exec())