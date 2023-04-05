from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout, QApplication, QWidget, QTableView, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QGroupBox, QScrollArea, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from font import FontLabel


class Rijbaan(QFrame):  #Tekst Rijbaan
     def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        label = QLabel("Rijbaan 1")
        label.setStyleSheet("border-bottom : 1px solid white ; border-radius : 0px ; padding-bottom : 4px" )
        self.layout.addWidget(label)
    
class Button(QPushButton):
    def __init__(self, text, icon=None, menu=None):
        super().__init__()
        self.setText(text)
        if icon:
            self.setIcon(QIcon(icon))
        if menu:
            self.setMenu(menu)


class Menu(QMenu):
    def __init__(self):
        super().__init__()
        self.optie1 = self.addAction("Optie 1")
        self.optie2 = self.addAction("Optie 2")
        self.optie3 = self.addAction("Optie 3")

class MatrixMenu(QMenu):
    def __init__(self):
        super().__init__()

        self.niets = self.addAction("Toon niets")
        self.roodKruis = self.addAction("Rood kruis")
        self.groenePijl = self.addAction("Groene pijl")
        self.pijlLinks = self.addAction("Pijl naar links")
        self.pijlRechts = self.addAction("Pijl naar rechts")
        self.einde = self.addAction("Einde beperkingen")
        self.flashOn = self.addAction("Flash aan")
        self.flashOff = self.addAction("Flash uit")
        self.show50 = self.addAction("50")
        self.show70 = self.addAction("70")
        self.show80 = self.addAction("80")
        self.show90 = self.addAction("90")
        self.show100 = self.addAction("100")

class Verkeerslichtknop(QPushButton):
    def __init__(self, icon):
        super().__init__()
        self.setIcon(QIcon(icon))


class VerkeerslichtMenu(QMenu):
    def __init__(self, gedoofd, rood):
        super().__init__()

        self.zet_gedoofd = self.addAction(QIcon("green_circle.png"), gedoofd)
        self.zet_rood = self.addAction(QIcon("red_circle.png"), rood)

class Bedieningen(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: 4c575b;")
        # Creating horizontal layout for buttons
        self.h_layout = QHBoxLayout()
        self.h_layout.setSpacing(10)
        self.h_layout2 = QHBoxLayout()
        self.h_layout2.setSpacing(10)

        self.button1 = Button("", "icons/alert-triangle.svg")
        
        self.button2 = Button("Bedrijf")
        self.button2.setMenu(Menu())
        self.button2.menu().optie1.triggered.connect(self.optie1)
        self.button2.menu().optie2.triggered.connect(self.optie2)
        self.button2.menu().optie3.triggered.connect(self.optie3)

        self.button3 = Button("")

        self.button5 = Button("Open")

        self.button6 = Button("Close")

        self.button4 = Verkeerslichtknop("icons/circle.svg")
        self.button4.setMenu(VerkeerslichtMenu("zet gedoofd", "zet rood"))

        self.button4.menu().zet_gedoofd.triggered.connect(self.gedoofdlicht)
        self.button4.menu().zet_rood.triggered.connect(self.roodlicht)

        self.button5.clicked.connect(self.change_button_text)
        self.button6.clicked.connect(self.change_button_text)

        self.MatrixStatus = Button("")
        self.SetMatrixStatus = Button("Set commando")
        self.SetMatrixStatus.setMenu(MatrixMenu())

        self.SetMatrixStatus.menu().niets.triggered.connect(lambda: self.ChangeStatus("Toon niets"))
        self.SetMatrixStatus.menu().roodKruis.triggered.connect(lambda: self.ChangeStatus("Rood kruis"))
        self.SetMatrixStatus.menu().groenePijl.triggered.connect(lambda: self.ChangeStatus("Groene pijl"))
        self.SetMatrixStatus.menu().pijlLinks.triggered.connect(lambda: self.ChangeStatus("Pijl naar links"))
        self.SetMatrixStatus.menu().pijlRechts.triggered.connect(lambda: self.ChangeStatus("Pijl naar rechts"))
        self.SetMatrixStatus.menu().einde.triggered.connect(lambda: self.ChangeStatus("Einde beperkingen"))
        self.SetMatrixStatus.menu().flashOn.triggered.connect(lambda: self.ChangeStatus("Flash aan"))
        self.SetMatrixStatus.menu().flashOff.triggered.connect(lambda: self.ChangeStatus("Flash uit"))
        self.SetMatrixStatus.menu().show50.triggered.connect(lambda: self.ChangeStatus("50"))
        self.SetMatrixStatus.menu().show70.triggered.connect(lambda: self.ChangeStatus("70"))
        self.SetMatrixStatus.menu().show80.triggered.connect(lambda: self.ChangeStatus("80"))
        self.SetMatrixStatus.menu().show90.triggered.connect(lambda: self.ChangeStatus("90"))
        self.SetMatrixStatus.menu().show100.triggered.connect(lambda: self.ChangeStatus("100"))

        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.h_layout.addWidget(self.button3)
        self.h_layout.addWidget(self.button4)
        self.h_layout.addWidget(self.button5)
        self.h_layout.addWidget(self.button6)
        self.h_layout2.addWidget(self.MatrixStatus)
        self.h_layout2.addWidget(self.SetMatrixStatus)

        verticale_layout = QVBoxLayout()
        verticale_layout.addLayout(self.h_layout)
        verticale_layout.addLayout(self.h_layout2)
        self.setLayout(verticale_layout)

    def change_button_text(self):
        sender = self.sender()
        if sender == self.button5:
            self.button3.setText("Opened")
        elif sender == self.button6:
            self.button3.setText("Closed")


    def roodlicht(self):
        print("RED")

    def gedoofdlicht(self):
        print("GEDOOFD")

    def optie1(self):
        print("Optie 1")
        #hier kunnen acties worden uitgevoerd

    def optie2(self):
        print("Optie 2")
        #hier kunnen acties worden uitgevoerd

    def optie3(self):
        print("Optie 3")
        #hier kunnen acties worden uitgevoerd

    def ChangeStatus(self, new_txt):
        self.MatrixStatus.setText(new_txt)

class Blokbedieningen(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color {color : #ffffff; background-color: #ffffff;border-radius: 5px;}")
        self.setContentsMargins(10,10,10,10)
        
        self.rijbaan_nummer = Rijbaan()
        self.bedieningsknoppen = Bedieningen()
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.rijbaan_nummer)
        self.layout.addWidget(self.bedieningsknoppen)
        self.layout.addItem(self.verticalstrech)
        self.setLayout(self.layout)


        
class PrimaireBediening(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #ffffff; background-color: #859faa;border-radius: 5px;}")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.bediening = Blokbedieningen()
        self.layout.addWidget(self.bediening)

       
