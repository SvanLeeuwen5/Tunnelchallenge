from PyQt6.QtWidgets import QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QComboBox, QHBoxLayout
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
        self.setFixedSize(120,34)
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
        self.stoplicht_status.setStyleSheet("QLabel {color : black; padding : 0px;  border: 1px solid black; background-color: #bac8ce; border-radius : 0px; border-top-left-radius : 2px; border-bottom-left-radius : 2px; border-right : 0px}")
        self.stoplicht_status.setFixedSize(40,40)
        self.stoplicht = StopLichtBox()

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
        self.layout.addItem(self.horizontalstretch)

    def changeStoplichtStatus(self, status):
        if status == 'red':
            self.stoplicht_status.setPixmap(QPixmap("icons/circle_red.svg").scaled(20,20))
            self.stoplicht_status.setText("")
        if status == 'yellow' or status == 'yellow_blinking':
            self.stoplicht_status.setPixmap(QPixmap("icons/circle_orange.svg").scaled(20,20))
            self.stoplicht_status.setText("")
        if status == 'off':
            self.stoplicht_status.setPixmap(QPixmap().scaled(20,20))
            self.stoplicht_status.setText("Uit")
            #self.stoplicht_status.setPixmap(QPixmap("icons/circle.svg").scaled(20,20))

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
        self.setMaximumWidth(600)
        self.setLayout(self.layout)

        self.rijbaan1Bediening = Blokbedieningen("Rijbaan 1")
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.layout.addWidget(self.rijbaan1Bediening)
        self.layout.addItem(self.verticalstrech)

       