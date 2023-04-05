from PyQt6.QtWidgets import QGridLayout, QFrame
from systemen_detecties_frame import SystemenDetecties
from meldinglijst_frame import MeldingLijst
from primaire_bediening import PrimaireBediening

#   TODO
#   Afsluitbomen
#   Verlichting
"""
Toestandsvariabelen                          Commando's

#richting: aflopend | oplopend                 SetAutoregeling(aan | uit)
#niveau: percentage                            SetStand(0..10)
#capaciteit_beschikbaar: percentage
#branduren: uren
"""
#   SOS
"""
Toestandsvariabelen                            Commando's

#snelheidsonderschrijdingen: locatie           SetEnabled(r: rijstrook, l1: lengtepositie, l2: lengtepositie, ja|nee):                                             
#spookrijders[]: locatie
#stilstanden[]: locatie
#disabled_detectiepunten[]: locatie                                                

"""
#   Verkeerslichten

#   MTM Borden

class OverzichtsPlattegrond(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #859faa;border-radius: 5px;}")

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
        self.overzichts_plattegrond = OverzichtsPlattegrond()
        self.melding_lijst = MeldingLijst()
        self.systemen_detecties = SystemenDetecties()

        self.primaire_bedieing.setMinimumSize(400,400)
        self.overzichts_plattegrond.setMinimumSize(400,400)
        self.melding_lijst.setMinimumSize(400,400)
        self.systemen_detecties.setMinimumSize(400,400) 

        self.layout.addWidget(self.primaire_bedieing, 0, 0)
        self.layout.addWidget(self.overzichts_plattegrond, 0, 1)
        self.layout.addWidget(self.melding_lijst, 1, 1)
        self.layout.addWidget(self.systemen_detecties, 1, 0)
