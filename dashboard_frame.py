from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from font import FontLabel

#   TODO
#   Afsluitbomen
#   Verlichting
"""
Toestandsvariabelen​                            Commando’s​

#richting: aflopend | oplopend​                 SetAutoregeling(aan | uit)​
#niveau: percentage​                            SetStand(0..8)​
#capaciteit_beschikbaar: percentage​
#branduren: uren​
"""
#   SOS
"""
Toestandsvariabelen​                            Commando's​

#snelheidsonderschrijdingen: locatie​           SetEnabled(r: rijstrook, l1: lengtepositie, l2: lengtepositie, ja|nee):​                                             
#spookrijders[]: locatie​
#stilstanden[]: locatie​
#disabled_detectiepunten[]: locatie                                                
​
"""
#   Verkeerslichten

#   MTM Borden

class MeldingLijst(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-radius: 5px;}")  

class SystemenDetectiesDetails(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)    

class SystemenDetectieButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("QPushButton {color : #000000; background-color: #4c575b; border : 0px; border-bottom : 1px solid #000000;}")
        self.setMinimumHeight(20)

class SystemenDetectiesFoldDetails(QFrame):
    def __init__(self, list):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {color : #000000; background-color: #4c575b; border : 0px;}")       
        self.setLayout(self.layout) 
        for str in list:
            self.layout.addWidget(SystemenDetectieButton(str)) 


class SystemenDetectieFoldButton(QPushButton):
    def __init__(self, text:str):
        super().__init__(text)
        self.setStyleSheet("QPushButton {color : #000000; background-color: #4c575b; border-bottom : 1px solid #000000; border-radius: 0px;}")
        self.setIcon(QIcon("icons/caret-right.svg"))
        self.setMinimumHeight(20)
        self.folded = True


class SystemenDetectiesList(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(4,4,4,4)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setFixedWidth(385)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-right: 1px solid black; border-left: 1px solid black;border-radius : 0px}")
        self.fold_button_buis = SystemenDetectieFoldButton("Buis")
        self.fold_button_buis.clicked.connect(self.buisActive)        
        self.fold_details_buis = SystemenDetectiesFoldDetails({"Ventilatie", "Verlichting", "CCTV"})
        self.fold_button_vluchtweg = SystemenDetectieFoldButton("Vluchtweg")
        self.fold_button_vluchtweg .clicked.connect(self.vluchtwegActive)
        self.fold_button_tunnel = SystemenDetectieFoldButton("Tunnel")
        self.fold_button_verkeer = SystemenDetectieFoldButton("Verkeer")
        self.fold_button_detecties= SystemenDetectieFoldButton("Detecties")

        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        self.layout.addWidget(self.fold_button_buis)
        self.layout.addWidget(self.fold_details_buis)
        self.layout.addWidget(self.fold_button_vluchtweg)
        self.layout.addWidget(self.fold_button_tunnel)
        self.layout.addWidget(self.fold_button_verkeer)
        self.layout.addWidget(self.fold_button_detecties)
        self.layout.addItem(self.verticalstrech)

        self.fold_details_buis.hide()

    def buisActive(self):
        if self.fold_button_buis.folded:
            self.fold_button_buis.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_buis.folded = False
            self.fold_details_buis.show()
        else:
            self.fold_button_buis.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_buis.folded = True
            self.fold_details_buis.hide()

    def vluchtwegActive(self):
        if self.fold_button_vluchtweg.folded:
            self.fold_button_vluchtweg.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_vluchtweg.folded = False
            #self.fold_details_buis.show()
        else:
            self.fold_button_vluchtweg.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_vluchtweg.folded = True
            #self.fold_details_buis.hide()        

class SystemenDetectiesFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,10,0,10)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-radius: 5px;}")
        self.horizontalstretch = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.systemen_detecties_list = SystemenDetectiesList()
        self.layout.addWidget(self.systemen_detecties_list)
        self.layout.addItem(self.horizontalstretch)



class SystemenDetecties(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet("color : #b2b2b2; background-color: #30393c; border: 1px solid black; border-radius: 5px;")

        self.setStyleSheet( "QTabBar:tab {height : 120px; width : 30px; color : #b2b2b2; background-color: #30393c; border-radius: 2px; font-size: 16px; border-top-left-radius: 5px;border-bottom-left-radius: 5px;}"
                            "QTabBar:tab:selected {color : #b2b2b2; background-color: #4c575b;}"
                            "QTabWidget::pane { border: 1px}")
        self.setTabPosition(QTabWidget.TabPosition.West)
        self.setTabIcon(1, QIcon("icons/square.svg"))
        self.setFixedWidth(800)
        self.re_frame = SystemenDetectiesFrame()
        self.wi_frame  = SystemenDetectiesFrame()
        self.h_li_frame = SystemenDetectiesFrame()
        self.p_li_frame = SystemenDetectiesFrame()
        self.dgb_frame = SystemenDetectiesFrame()
        self.addTab(self.re_frame, "Re")
        self.addTab(self.wi_frame, "Wi")
        self.addTab(self.h_li_frame, "H Li")
        self.addTab(self.p_li_frame, "P Li")
        self.addTab(self.dgb_frame, "DGB")

class OverzichtsPlattegrond(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;border-radius: 5px;}")

class PrimaireBediening(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;border-radius: 5px;}")

class DetailPlattegrond(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c;border-radius: 5px;}")


class DashboardFrame(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #000000;}")
        self.setContentsMargins(10,10,10,10)
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0,0,0,10)
        self.setLayout(self.layout)
        self.addFrames()

    def addFrames(self):
        self.primaire_bedieing = PrimaireBediening()
        self.detail_plattegrond = DetailPlattegrond()
        self.overzichts_plattegrond = OverzichtsPlattegrond()
        self.melding_lijst = MeldingLijst()
        self.systemen_detecties = SystemenDetecties()

        self.layout.addWidget(self.primaire_bedieing, 0, 0)
        self.layout.addWidget(self.overzichts_plattegrond, 0, 1)
        self.layout.addWidget(self.detail_plattegrond, 2, 1)
        self.layout.addWidget(self.melding_lijst, 1, 1)
        self.layout.addWidget(self.systemen_detecties, 1, 0, 2, 1)
