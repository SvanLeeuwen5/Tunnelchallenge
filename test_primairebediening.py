from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout, QApplication, QWidget, QTableView, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QGroupBox, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from font import FontLabel


class Rijbaan(QFrame):  #Tekst Rijbaan
     def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        label = QLabel("Rijbaan 1  ________________________________________________")
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.layout.addWidget(label)
        self.layout.addItem(self.verticalstrech)

class PrimaireBedieningButton(QFrame):
    def __init__(self, text):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {color : #000000; background-color: #4c575b; border : 0px;border-bottom : 1px solid #2c2c2c;}"
                           "QPushButton {color : #000000; background-color: #4c575b; border : 0px; text-align: left; padding-left : 50px}"
                           "QLabel {color : #000000; background-color: #4c575b; border : 0px; }")       
        self.setLayout(self.layout) 
        self.setMinimumHeight(20)
        self.setMinimumHeight(20)
        self.button = QPushButton(text)
        self.button.setMinimumWidth(150)
        self.icon1 = QLabel("")
        self.icon1.setPixmap(QIcon("icons/circle.svg").pixmap(15,15)) #deze moet een groene cirkel zijn
        self.icon1.setFixedSize(20,20)
        self.icon2 = QLabel("")
        self.icon2.setPixmap(QIcon("icons/circle.svg").pixmap(15,15))  # deze moet een rode cirkel zijn
        self.icon2.setFixedSize(20,20)
        self.icon3 = QLabel("")
        self.icon3.setPixmap(QIcon("icons/triangle.svg").pixmap(15,15)) # Rode uitroepteken
        self.icon3.setFixedSize(20,20)
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.button)
        # self.layout.addWidget(self.icon1)  # --> voor button 1
        # self.layout.addWidget(self.icon2)  # --> voor button 4 (groen licht)
        # self.layout.addWidget(self.icon3)  # --> voor button 4 (rood)
        self.layout.addItem(self.horizontalSpacer)

class PrimaireBedieningFoldDetails(QFrame):
    def __init__(self, list):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {color : #000000; background-color: #4c575b; border : 0px;}")       
        self.setLayout(self.layout) 
        for name in list:
            self.layout.addWidget(PrimaireBedieningButton(name)) 

class PrimaireBedieningFoldButton(QFrame):
    def __init__(self, text):
        super().__init__()
        self.setStyleSheet("QFrame {color : #000000; background-color: #4c575b; border : 0px; border-bottom : 1px solid #000000;border-top : 2px solid #000000; border-radius: 0px;}"
                           "QPushButton {color : #000000; background-color: #4c575b; text-align: left; border : 0px;}"
                           "QLabel {color : #000000; background-color: #4c575b; border: 0px; border-bottom : 1px solid #000000; border-top : 2px solid #000000;}")
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setMinimumHeight(20)
        self.button = QPushButton(text)
        self.button.setMinimumWidth(100)
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.button)
        self.layout.addItem(self.horizontalSpacer)

        self.folded = True


    
class BedieningsknoppenLijst(QFrame): #knoppen
    def __init__(self):
        super().__init__()
        self.setContentsMargins(4,4,4,4)
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setFixedWidth(300)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-right: 1px solid black; border-left: 1px solid black;border-radius : 0px}")

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button3 = QPushButton("Button 3")
        self.layout.addWidget(self.button3)

        self.fold_button_buis = PrimaireBedieningFoldButton("Bedrijf")
        self.fold_button_buis.button.clicked.connect(self.BedrijfActive)        
        self.fold_details_buis = PrimaireBedieningFoldDetails({"Test1", "Test2", "Test3"})
  
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        self.layout.addWidget(self.fold_button_buis)
        self.layout.addWidget(self.fold_details_buis)

        self.layout.addItem(self.verticalstrech)

        self.fold_details_buis.hide()
    
        


    def BedrijfActive(self):
        if self.fold_button_buis.folded:
            self.fold_button_buis.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_buis.folded = False
            self.fold_details_buis.show()
        else:
            self.fold_button_buis.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_buis.folded = True
            self.fold_details_buis.hide()

    



    #  def __init__(self):
    #     super().__init__()
    #     self.layout = QHBoxLayout()

    #     self.button1 = QPushButton("Button1")
    #     self.button2 = QPushButton("Button 2")
    #     self.layout.addWidget(self.button1)
    #     self.layout.addWidget(self.button2)
    #     self.layout.addStretch(1)
    #     self.setLayout(self.layout)

    #     size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    #     self.setSizePolicy(size_policy)


class Blokbedieningen(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color {color : #ffffff; background-color: #859faa;border-radius: 5px;}")
        self.setContentsMargins(10,10,10,10)
        
        self.rijbaan_nummer = Rijbaan()
        self.bedieningsknoppen = BedieningsknoppenLijst()

        self.layout = QGridLayout()
        self.layout.addWidget(self.rijbaan_nummer)
        self.layout.addWidget(self.bedieningsknoppen)
        self.setLayout(self.layout)


        
class PrimaireBediening(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;border-radius: 5px;}")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.bediening = Blokbedieningen()
        self.layout.addWidget(self.bediening)

       
