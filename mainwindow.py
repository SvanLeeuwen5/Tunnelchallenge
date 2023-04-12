from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt6.QtCore import QMargins, QTimer
from PyQt6.QtGui import QPixmap
from menu_frame import Menu
from camera_frame import CameraFrame
from dashboard_frame import DashboardFrame
from login_frame import LoginFrame
from data_parse import DataParser
import sys
import requests

class mainwindow(QWidget):
    """
    This is the main window of the application.
    All functions reside within this class.
    """
    def __init__(self):
        super(mainwindow, self).__init__()
        self.lastSize = self.size()
        #self.data = DataParser()
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
            #VERLICHTING
        verlichting = self.data.lighting_state
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.niveau.setWaarde(verlichting[0]) 
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.capaciteit.setWaarde(verlichting[1])
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.energieverbruik.setWaarde(verlichting[2])
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.branduren.setWaarde(verlichting[3])
            #CCTV
        cctv = self.data.cctv_state
        self.camera_window.controlpanel.panel_camera1.option_slider_pan.setValue(cctv[0])
        self.camera_window.controlpanel.panel_camera1.option_slider_tilt.setValue(cctv[1])
        self.camera_window.controlpanel.panel_camera1.option_slider_zoom.setValue(cctv[2])
        self.camera_window.controlpanel.panel_camera1.option_slider_preset.setValue(cctv[3])
            #VRI
        vri = self.data.vri_state
        self.dashboard_window.systemen_detecties.rijbaan1.verkeerslicht_details.state.setWaarde(vri[0])
        self.dashboard_window.systemen_detecties.rijbaan1.verkeerslicht_details.beschikbaarheid.setWaarde(vri[1])
        self.dashboard_window.systemen_detecties.rijbaan1.verkeerslicht_details.error.setWaarde(vri[2])
            #BARRIER
        barrier = self.data.barrier_state
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.state.setWaarde(barrier[0])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.beschikbaarheid.setWaarde(barrier[1])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.movement.setWaarde(barrier[2])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.obstacle.setWaarde(barrier[3])
        self.dashboard_window.systemen_detecties.rijbaan1.slagboom_details.error.setWaarde(barrier[4])
            #MATRIX
        matrix = self.data.msi_state
        self.dashboard_window.overzichts_plattegrond.matrix1.matrixbord.setStatus(matrix[0])
        self.dashboard_window.overzichts_plattegrond.matrix2.matrixbord.setStatus(matrix[1])
        self.dashboard_window.overzichts_plattegrond.matrix3.matrixbord.setStatus(matrix[2])
        self.dashboard_window.overzichts_plattegrond.matrix4.matrixbord.setStatus(matrix[3])
            #SENSOR
        #sensor = self.data.sensor_state
        #self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.CO.setWaarde(barrier[0])
        #self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.CO2.setWaarde(barrier[1])
        #self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.NO2.setWaarde(barrier[2])

    def connectCameraSliders(self):
<<<<<<< Updated upstream
        self.camera_window.controlpanel.panel_camera1.option_slider_pan.valueChanged.connect(self.changePan)
        self.camera_window.controlpanel.panel_camera1.option_slider_tilt.valueChanged.connect(self.changeTilt)
        self.camera_window.controlpanel.panel_camera1.option_slider_zoom.valueChanged.connect(self.changeZoom)
        self.camera_window.controlpanel.panel_camera1.option_slider_preset.valueChanged.connect(self.changePreset)
=======
        self.camera_window.controlpanel.panel_camera1.confirm_button.clicked.connect(self.changeCamera)
        self.camera_window.controlpanel.panel_camera2.confirm_button.clicked.connect(self.changeCamera)
>>>>>>> Stashed changes

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
        if self.camera_window.controlpanel.panel_camera1.option_slider_preset.value() == 0:
            requests.get("http://192.168.10.199/axis-cgi/com/ptz.cgi?gotoserverpresetname=Home&camera=1")
        if self.camera_window.controlpanel.panel_camera1.option_slider_preset.value() == 1:
            requests.get("http://192.168.10.199/axis-cgi/com/ptz.cgi?gotoserverpresetname=Ingang&camera=1")
        if self.camera_window.controlpanel.panel_camera1.option_slider_preset.value() == 2:
            requests.get("http://192.168.10.199/axis-cgi/com/ptz.cgi?gotoserverpresetname=Uitgang&camera=1")
        if self.camera_window.controlpanel.panel_camera1.option_slider_preset.value() == 3:
            requests.get("http://192.168.10.199/axis-cgi/com/ptz.cgi?gotoserverpresetname=Podium&camera=1")
        if self.camera_window.controlpanel.panel_camera2.option_slider_preset.value() == 0:
            requests.get("http://192.168.10.99/axis-cgi/com/ptz.cgi?gotoserverpresetname=Home&camera=1")
        if self.camera_window.controlpanel.panel_camera2.option_slider_preset.value() == 1:
            requests.get("http://192.168.10.99/axis-cgi/com/ptz.cgi?gotoserverpresetname=Ingang&camera=1")
        if self.camera_window.controlpanel.panel_camera2.option_slider_preset.value() == 2:
            requests.get("http://192.168.10.99/axis-cgi/com/ptz.cgi?gotoserverpresetname=Uitgang&camera=1")
        if self.camera_window.controlpanel.panel_camera2.option_slider_preset.value() == 3:
            requests.get("http://192.168.10.99/axis-cgi/com/ptz.cgi?gotoserverpresetname=Tafeltje&camera=1")
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
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Open")
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(True)
        else:
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setChecked(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(True)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Open")
        #barrier = self.data.barrier_state
        #if barrier[0] == 1:
            #self.data.Control_Barrier(0,'up')

    def closeSlagboom(self):
        if self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.isChecked() == False:
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Dicht")
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(True)
        else:
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setChecked(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.slagboom_status.setText("Dicht")  
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_close.setEnabled(False)
            self.dashboard_window.primaire_bediening.rijbaan1Bediening.bedieningsknoppen.button_open.setEnabled(True)     
        #barrier = self.data.barrier_state
        #if barrier[0] == 0:
            #self.data.Control_Barrier(0,'down')

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