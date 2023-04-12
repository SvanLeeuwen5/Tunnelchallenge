from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QComboBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer
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
    def __init__(self, matrixbord, status=0, flashstatus=0):
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

        self.matrixbord = Matrixbord(self, status, flashstatus)
        self.matrixBesturing =BesturingFrame()
        
        self.layout.addWidget(self.matrix_label,0,0)
        self.layout.addWidget(self.matrixbord,1,0)
        self.layout.addWidget(self.matrixBesturing,1,1)

class Matrixbord(QFrame):
    def __init__(self, parent, status, flash):
        super().__init__()
        self.parent = parent
        self.setFixedSize(160, 160)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #2c2c2c ;border-radius: 5px;}")
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,1)
        self.layout.setColumnStretch(2,1)
        self.layout.setRowStretch(0,1)
        self.layout.setRowStretch(1,1)
        self.layout.setRowStretch(2,1)

        self.label = FontLabel("", 45, True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flashLabel1 = FontLabel("", 10, True)
        self.flashLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flashLabel2 = FontLabel("", 10, True)
        self.flashLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flashLabel3 = FontLabel("", 10, True)
        self.flashLabel3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flashLabel4 = FontLabel("", 10, True)
        self.flashLabel4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStatus(status, flash)
        
        self.layout.addWidget(self.flashLabel1,0,0)
        self.layout.addWidget(self.flashLabel2,0,2)
        self.layout.addWidget(self.flashLabel3,2,0)
        self.layout.addWidget(self.flashLabel4,2,2)
        self.layout.addWidget(self.label,1,1)
        self.setLayout(self.layout)

    def setFlash(self, status):
        self.timer = QTimer()
        self.icon = QIcon('icons/circle_orange')

        if status == "on": #Flash On    
            self.flashLabel1.setPixmap(self.icon.pixmap(20, 20))
            self.flashLabel2.setPixmap(self.icon.pixmap(20, 20))
            self.flashLabel3.setPixmap(QPixmap())
            self.flashLabel4.setPixmap(QPixmap())
            self.timer.timeout.connect(self.ToggleDown)
            self.timer.start(1000)
        
        if status == "off": #Flash Off
            self.timer.stop
            self.flashLabel1.setPixmap(QPixmap())
            self.flashLabel2.setPixmap(QPixmap())
            self.flashLabel3.setPixmap(QPixmap())
            self.flashLabel4.setPixmap(QPixmap())


    def ToggleUp(self):
        self.flashLabel1.setPixmap(self.icon.pixmap(20, 20))
        self.flashLabel2.setPixmap(self.icon.pixmap(20, 20))
        self.flashLabel3.setPixmap(QPixmap())
        self.flashLabel4.setPixmap(QPixmap())
        self.timer.timeout.connect(self.ToggleDown)

    def ToggleDown(self):
        self.flashLabel1.setPixmap(QPixmap())
        self.flashLabel2.setPixmap(QPixmap())
        self.flashLabel3.setPixmap(self.icon.pixmap(20, 20))
        self.flashLabel4.setPixmap(self.icon.pixmap(20, 20))
        self.timer.timeout.connect(self.ToggleUp)

    def setStatus(self, status, flash="off"): 
        self.setFlash(flash)
        if status == "red_cross":
            self.label.setText("")
            self.icon = QIcon('icons/red-cross')
            self.label.setPixmap(self.icon.pixmap(160, 160))
        elif status == "green_arrow":
            self.label.setText("")
            self.icon = QIcon('icons/green-arrow')
            self.label.setPixmap(self.icon.pixmap(160, 160))
        elif status == "arrow_left":
            self.label.setText("")
            self.icon = QIcon('icons/arrow-left')
            self.label.setPixmap(self.icon.pixmap(160, 160))
        elif status == "arrow_right":
            self.label.setText("")
            self.icon = QIcon('icons/arrow-right')
            self.label.setPixmap(self.icon.pixmap(160, 160))
        elif status == "end_limitation":
            self.label.setText("")
            self.icon = QIcon('icons/end-signal')
            self.label.setPixmap(self.icon.pixmap(160, 160))
        elif status == "50":
            self.label.setPixmap(QPixmap())
            self.label.setText("50")
        elif status == "70":
            self.label.setPixmap(QPixmap())
            self.label.setText("70")
        elif status == "80":
            self.label.setPixmap(QPixmap())
            self.label.setText("80")
        elif status == "90":
            self.label.setPixmap(QPixmap())
            self.label.setText("90")
        elif status == "100":
            self.label.setPixmap(QPixmap())
            self.label.setText("100")
        
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
        self.matrix = MatrixFrame("Matrixbord", "off", "off")

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,1)
        self.layout.setRowStretch(0,1)
        self.layout.setRowStretch(1,1)

        self.layout.addWidget(self.matrix,0,0)
        
        #self.tmp = QTimer()
        #self.tmp.start(10000)
        #self.tmp.timeout.connect(self.TMP)

    #def TMP(self):
        #self.matrix.matrixbord.setFlash("off")
        #self.tmp.stop