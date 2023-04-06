from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QComboBox, QHBoxLayout, QApplication, QWidget, QTableView, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QGroupBox, QScrollArea, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon,QPixmap, QFont
from font import FontLabel
    

class StopLichtBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem("Rood")
        self.addItem("Uitschakelen")
        self.setFixedSize(18,40)
        self.setStyleSheet("QComboBox::down-arrow { image: url(icons/caret-down.svg);}"
                           "QComboBox::drop-down {width : 20px; color: white; border: 1px solid black; background-color: #bac8ce; border-radius : 0px; border-top-right-radius : 2px; border-bottom-right-radius : 2px; border-left : 1px solid #818181}"
                           "QComboBox QAbstractItemView {min-width : 100px; background-color: #bac8ce;color: black; border: 1px solid black; }")

class RijbaanstatusBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem("Bedrijf")
        self.addItem("Evacueren")
        self.addItem("Ondersteunend")
        self.setFixedSize(100,34)
        self.setFont(QFont("Nirmala UI", 10))
        self.setStyleSheet("QComboBox { color: white ; border: 1px solid #111111; background-color: black; border-radius : 1px;}"
                           "QComboBox QAbstractItemView { color: white; border: 1px solid #111111; background-color: black; border-radius : 1px;}")        
        
class MatrixbordstatusBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem("Zet uit")                 #0 : toon niets
        self.addItem("Sluit rijbaan")           #1 : Rood kruis
        self.addItem("Open rijbaan")            #2 : Groene pijl
        self.addItem("Pijl naar links")         #3 : Witte drijfpijl naar links
        self.addItem("Pijl naar rechts")        #4 : Witte drijfpijl naar rechts
        self.addItem("Einde beperkingen")       #5 : Witte cirkel met schuine streep
        self.addItem("Flash aan")               #6 : Flash aan
        self.addItem("Flash uit")               #7 : Flash uit
        self.addItem("Rijsnelheid 50")          #50 : 50 in wit
        self.addItem("Rijsnelheid 70")          #70 : 70 in wit
        self.addItem("Rijsnelheid 80")          #80 : 80 in wit
        self.addItem("Rijsnelheid 90")          #90 : 90 in wit
        self.addItem("Rijsnelheid 100")         #100 : 100 in wit
        self.setFixedSize(140,34)
        self.setFont(QFont("Nirmala UI", 10))
        self.setStyleSheet("QComboBox { color: white ; border: 1px solid #111111; background-color: black; border-radius : 1px;}"
                           "QComboBox QAbstractItemView { color: white; border: 1px solid #111111; background-color: black; border-radius : 1px;}")        
        

class IconButton(QPushButton):
    def __init__(self, icon):
        super().__init__()
        self.setIcon(QIcon(icon))
        self.setFixedSize(40,40)
        self.setCheckable(True)
        self.setChecked(False)
        self.setStyleSheet("QPushButton { margin : 0px; border: 1px solid black; background-color: #bac8ce; border-radius : 2px;}"
                           "QPushButton:checked { background-color: #c6a64c; border: 1px solid black;}")

class TextButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(40,40)
        self.setCheckable(True)
        self.setChecked(False)


class Bedieningen(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10,10,10,10)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)


        self.noodstop = IconButton("icons/alert-triangle.svg")
        
        self.rijbaan_status = RijbaanstatusBox()

        self.slagboom_status = FontLabel("Open", 10, False)
        self.slagboom_status.setStyleSheet("FontLabel {color : white; background-color: black; border : 0px; border-radius : 1px;}")
        self.slagboom_status.setFixedSize(60,34)
        self.button_open = TextButton("Open")
        self.button_open.setStyleSheet("QPushButton { margin : 0px; border: 1px solid black; background-color: #bac8ce; border-radius : 2px;border-top-left-radius : 0px; border-bottom-left-radius : 0px; border-left : 0px}"
                                       "QPushButton:checked { background-color: #c6a64c; border: 1px solid black;}")
        self.button_close = TextButton("Sluit")
        self.button_close.setStyleSheet("QPushButton { margin : 0px; border: 1px solid black; background-color: #bac8ce; border-radius : 2px;  border-top-right-radius : 0px; border-bottom-right-radius : 0px; border-right : 1px solid #818181}"
                                        "QPushButton:checked { background-color: #c6a64c; border: 1px solid black;}")
        self.stoplicht_status = QLabel()
        self.stoplicht_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stoplicht_status.setStyleSheet("QLabel {padding : 0px;  border: 1px solid black; background-color: #bac8ce; border-radius : 0px; border-top-left-radius : 2px; border-bottom-left-radius : 2px; border-right : 0px}")
        self.stoplicht_status.setFixedSize(40,40)
        self.stoplicht = StopLichtBox()
        self.changeStoplichtStatus()

        self.matrix_status = FontLabel("Toon niets", 10, False)
        self.matrix_status.setStyleSheet("FontLabel {color : white; background-color: black; border : 0px; border-radius : 1px;}")
        self.matrix_status.setFixedSize(120,34)
        self.matrix = MatrixbordstatusBox()
        self.changeMatrixStatus()


        self.horizontalstretch_4 = QSpacerItem(4,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
        self.horizontalstretch_40 = QSpacerItem(40,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
        self.horizontalstretch = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.noodstop)
        self.layout.addItem(self.horizontalstretch_4)
        self.layout.addWidget(self.rijbaan_status)
        self.layout.addItem(self.horizontalstretch_40)
        self.layout.addWidget(self.slagboom_status)
        self.layout.addItem(self.horizontalstretch_4)
        self.layout.addWidget(self.stoplicht_status)
        self.layout.addWidget(self.stoplicht)
        self.layout.addItem(self.horizontalstretch_4)
        self.layout.addWidget(self.button_close)
        self.layout.addWidget(self.button_open)
        self.layout.addItem(self.horizontalstretch_4)
        self.layout.addWidget(self.matrix_status)
        self.layout.addItem(self.horizontalstretch_4)
        self.layout.addWidget(self.matrix)
        

        self.button_open.clicked.connect(self.setSlagboomStatusOpen)
        self.button_close.clicked.connect(self.setSlagboomStatusClosed)

        self.stoplicht.currentIndexChanged.connect(self.changeStoplichtStatus)
        self.matrix.currentIndexChanged.connect(self.changeMatrixStatus)


    def changeStoplichtStatus(self):
        if self.stoplicht.currentIndex() == 0:
            self.stoplicht_status.setPixmap(QPixmap("icons/circle_red.svg").scaled(20,20))
        if self.stoplicht.currentIndex() == 1:
            self.stoplicht_status.setPixmap(QPixmap("icons/circle_orange.svg").scaled(20,20))

    def changeMatrixStatus(self):
        self.matrix_status.setText(self.matrix.currentText())

    def setSlagboomStatusOpen(self):
        if self.button_close.isChecked() == False:
            self.slagboom_status.setText("Open")
        else:
            self.button_close.setChecked(False)
            self.slagboom_status.setText("Open")

    def setSlagboomStatusClosed(self):
        if self.button_open.isChecked() == False:
            self.slagboom_status.setText("Dicht")
        else:
            self.button_open.setChecked(False)
            self.slagboom_status.setText("Dicht")       



class Blokbedieningen(QFrame):
    def __init__(self, text):
        super().__init__()
        self.setStyleSheet("FontLabel {padding : 4px; border-bottom: 1px solid white;border-radius: 0px;}")
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        self.rijbaan_nummer = FontLabel(text, 14, True)
        self.bedieningsknoppen = Bedieningen()

        self.layout.addWidget(self.rijbaan_nummer)
        self.layout.addWidget(self.bedieningsknoppen)

        
class PrimaireBediening(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10,10,10,10)
        self.setStyleSheet("QFrame {color : #ffffff; background-color: #859faa; border-radius: 5px;}")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.rijbaan1Bediening = Blokbedieningen("Rijbaan 1")
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.layout.addWidget(self.rijbaan1Bediening)
        self.layout.addItem(self.verticalstrech)

       
