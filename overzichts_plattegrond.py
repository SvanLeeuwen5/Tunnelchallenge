from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QComboBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QFont
from font import FontLabel

class Button(QPushButton):
    def __init__(self, text, icon=None, menu=None):
        super().__init__()
        self.setText(text)
        if icon:
            self.setIcon(QIcon(icon))
        if menu:
            self.setMenu(menu)

class MatrixFrame(QFrame):
    def __init__(self, matrixbord, status):
        super().__init__()
        self.setStyleSheet("QFrame {color : white; background-color: #859faa;}")
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.matrix_label = FontLabel(matrixbord, 15, True)
        self.matrix_label.setMaximumHeight(40)

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,1)
        self.layout.setRowStretch(0,1)
        self.layout.setRowStretch(1,1)

        self.hLayout = QHBoxLayout()
        self.hLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.hLayout.addWidget(self.matrix_label)
        self.setFlash(status)

        self.matrixbord = Matrixbord(status)
        self.matrixBesturing =BesturingFrame()
        
        self.layout.addLayout(self.hLayout,0,0)
        self.layout.addWidget(self.matrixbord,1,0)
        self.layout.addWidget(self.matrixBesturing,1,1)

    def setFlash(self, status):
        self.label = QLabel()

        if status == 6: #Flash On    
            self.icon = QIcon('icons/flash-on')
            self.label.setPixmap(self.icon.pixmap(160, 160))
            self.hLayout.addWidget(self.label)
        
        if status == 7: #Flash Off
            self.icon = QIcon('icons/flash-off')
            self.label.setPixmap(self.icon.pixmap(160, 160))
            self.hLayout.addWidget(self.label)

class Matrixbord(QFrame):
    def __init__(self, status):
        super().__init__()
        self.setFixedSize(160, 160)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #2c2c2c ;border-radius: 5px;}")
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStatus(status)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def setStatus(self, status):
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        if status < 50:
        
            if status == 1:
                self.icon = QIcon('icons/red-cross')
                self.label.setPixmap(self.icon.pixmap(160, 160))
            elif status == 2:
                self.icon = QIcon('icons/green-arrow')
                self.label.setPixmap(self.icon.pixmap(160, 160))
            elif status == 3:
                self.icon = QIcon('icons/arrow-left')
                self.label.setPixmap(self.icon.pixmap(160, 160))
            elif status == 4:
                self.icon = QIcon('icons/arrow-right')
                self.label.setPixmap(self.icon.pixmap(160, 160))
            elif status == 5:
                self.icon = QIcon('icons/end-signal')
                self.label.setPixmap(self.icon.pixmap(160, 160))
        else:
            if status == 50:
                self.label = FontLabel("50", 60, True)
            elif status == 70:
                self.label = FontLabel("70", 60, True)
            elif status == 80:
                self.label = FontLabel("80", 60, True)
            elif status == 90:
                self.label = FontLabel("90", 60, True)
            elif status == 100:
                self.label = FontLabel("100", 60, True)
            
            self.label.setStyleSheet("color: white; font: bold;")

class MatrixStatus(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem("Zet uit / toon niets")
        self.addItem("Sluit rijbaan")
        self.addItem("Open rijbaan")
        self.addItem("Rijbaan naar links")
        self.addItem("Rijbaan naar rechts")
        self.addItem("Einde beperkingen")
        self.addItem("Snelheidslimiet 50")
        self.addItem("Snelheidslimiet 70")
        self.addItem("Snelheidslimiet 80")
        self.addItem("Snelheidslimiet 90")
        self.addItem("Snelheidslimiet 100")
        self.setFixedSize(150,34)
        self.setFont(QFont("Nirmala UI", 10))
        self.setStyleSheet("QComboBox { color: white ; border: 1px solid #111111; background-color: black; border-radius : 1px;}"
                           "QComboBox QAbstractItemView { color: white; border: 1px solid #111111; background-color: black; border-radius : 1px;}")        
        
class FlashStatus(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem("Zet flash aan")
        self.addItem("Zet flash uit")
        self.setFixedSize(120,34)
        self.setFont(QFont("Nirmala UI", 10))
        self.setStyleSheet("QComboBox { color: white ; border: 1px solid #111111; background-color: black; border-radius : 1px;}"
                           "QComboBox QAbstractItemView { color: white; border: 1px solid #111111; background-color: black; border-radius : 1px;}")        
        

class BesturingFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        self.matrix_status = MatrixStatus()
        self.matrix_flashStatus = FlashStatus()

        self.layout.addWidget(self.matrix_status)
        self.layout.addWidget(self.matrix_flashStatus)
            
class OverzichtsPlattegrond(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;border-radius: 5px;}")
        self.setContentsMargins(10,10,10,10)
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.addFrames()

    def addFrames(self):
        self.matrix = MatrixFrame("Matrixbord", 0)

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,1)
        self.layout.setRowStretch(0,1)
        self.layout.setRowStretch(1,1)

        self.layout.addWidget(self.matrix,0,0)