from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import Qt
from font import FontLabel

class DashboardFrame(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #2c2c2c;}")
        self.setContentsMargins(50,30,50,30)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(0,0,0,10)
        self.setLayout(self.layout)
        self.addFrames()

    def addFrames(self):
        pass