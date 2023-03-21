from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import Qt
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
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c;}")  

class SystemenDetecties(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c;}")


class OverzichtsPlattegrond(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;}")

class PrimaireBediening(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;}")

class DetailPlattegrond(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c;}")


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
