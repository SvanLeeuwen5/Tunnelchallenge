from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import QMargins, Qt
from PyQt6.QtGui import QFont, QMouseEvent
from menu_frame import Menu
from camera_frame import CameraFrame
from dashboard_frame import DashboardFrame


class mainwindow(QWidget):
    """
    This is the main window of the application.
    All functions reside within this class.
    """
    def __init__(self):
        super(mainwindow, self).__init__()
        self.lastSize = self.size()
        self.initUI()
        self.createLayout()
        self.addPages()
        self.dashboardActive()
        self.connectButtons()
        self.show()   

    def initUI(self):
        self.setGeometry(300, 100, 1670, 1050)      

    def createLayout(self):
        self.mainwindow_layout = QGridLayout()
        self.mainwindow_layout.setSpacing(0)
        self.mainwindow_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.setLayout(self.mainwindow_layout)

    def addPages(self):
        self.menu = Menu(self)
        self.camera_window = CameraFrame()
        self.dashboard_window = DashboardFrame(self)
        
        self.mainwindow_layout.addWidget(self.menu, 0, 0)
        self.mainwindow_layout.addWidget(self.camera_window, 0, 1)
        self.mainwindow_layout.addWidget(self.dashboard_window, 0, 1)

    def connectButtons(self):
        self.menu.button_dashboard.clicked.connect(self.dashboardActive)
        self.menu.button_camera.clicked.connect(self.cameraActive)

    def dashboardActive(self):
        self.menu.button_dashboard.contentActive(True)
        self.menu.button_camera.contentActive(False)
        self.dashboard_window.show()
        self.camera_window.hide()

    def cameraActive(self):
        self.menu.button_dashboard.contentActive(False)
        self.menu.button_camera.contentActive(True)
        self.dashboard_window.hide()
        self.camera_window.show()


if __name__ == '__main__':
    app = QApplication([])
    mw = mainwindow()
    mw.move
    app.exec()