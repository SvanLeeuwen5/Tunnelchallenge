from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import QMargins, Qt, QTimer
from PyQt6.QtGui import QFont, QMouseEvent
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
        #self.data = DataParser()
        self.initUI()
        self.createLayout()
        self.addPages()
        self.dashboardActive()
        self.connectButtons()
        #self.refreshData()
        #self.setTimer()
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

    def connectButtons(self):
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
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.niveau.setWaarde(verlichting.niveau) 
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.capaciteit.setWaarde(verlichting.capaciteit)
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.energieverbruik.setWaarde(verlichting.energieverbruik)
        self.dashboard_window.systemen_detecties.rijbaan1.verlichting_details.branduren.setWaarde(verlichting.branduren)
        #CCTV
        cctv = self.data.cctv_state
        self.camera_window.controlpanel.panel_camera1.option_slider_pan.setValue(cctv.pan)
        self.camera_window.controlpanel.panel_camera1.option_slider_tilt.setValue(cctv.tilt)
        self.camera_window.controlpanel.panel_camera1.option_slider_zoom.setValue(cctv.zoom)
        self.camera_window.controlpanel.panel_camera1.option_slider_preset.setValue(cctv.preset)
        #VRI
        vri = self.data.vri_state
        self.dashboard_window.systemen_detecties.rijbaan1.stoplichting_details.state.setWaarde(vri.state)
        self.dashboard_window.systemen_detecties.rijbaan1.stoplichting_details.availability.setWaarde(vri.availability)
        self.dashboard_window.systemen_detecties.rijbaan1.stoplichting_details.error.setWaarde(vri.error)
        #BARRIER
        barrier = self.data.barrier_state
        self.dashboard_window.systemen_detecties.rijbaan1.barrier_details.state.setWaarde(barrier.state)
        self.dashboard_window.systemen_detecties.rijbaan1.barrier_details.availability.setWaarde(barrier.availability)
        self.dashboard_window.systemen_detecties.rijbaan1.barrier_details.movement.setWaarde(barrier.movement)
        self.dashboard_window.systemen_detecties.rijbaan1.barrier_details.obstacle.setWaarde(barrier.obstacle)
        self.dashboard_window.systemen_detecties.rijbaan1.barrier_details.error.setWaarde(barrier.error)
        #MATRIX
        matrix = self.data.msi_state
        self.dashboard_window.overzichts_plattegrond.matrix1.matrixbord.setStatus(matrix.status)
        self.dashboard_window.overzichts_plattegrond.matrix2.matrixbord.setStatus(matrix.status)
        self.dashboard_window.overzichts_plattegrond.matrix3.matrixbord.setStatus(matrix.status)
        self.dashboard_window.overzichts_plattegrond.matrix4.matrixbord.setStatus(matrix.status)
        #SENSOR
        sensor = self.data.sensor_state
        self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.CO.setWaarde(barrier.CO)
        self.dashboard_window.systemen_detecties.rijbaan1.sensor1_details.CO2.setWaarde(barrier.CO2)




        	



if __name__ == '__main__':
    app = QApplication([])
    mw = mainwindow()
    mw.move
    sys.exit(app.exec())