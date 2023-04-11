from PyQt6.QtWidgets import QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from font import FontLabel


class SystemenDetectiesDetails(QFrame):
    def __init__(self,text):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10,4,10,4)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)  
        self.setMinimumWidth(275)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-radius : 0px; border-right : 1px solid black;}")
        self.detail_frame = QFrame()
        self.detail_frame.setContentsMargins(10,0,10,0)
        
        self.detail_frame_layout = QVBoxLayout()
        self.detail_frame.setLayout(self.detail_frame_layout)
        self.detail_frame.setStyleSheet("QFrame {color : #b2b2b2; background-color: #4c575b; border : 0px; border-bottom : 1px solid #000000;border-top : 2px solid #000000; }"
                                        "FontLabel {color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.label = FontLabel(text, 10, True)
        self.detail_frame_layout.addWidget(self.label)
        self.layout.addWidget(self.detail_frame)

class SystemenDetectiesDetailsWaardeLabel(QFrame):
    def __init__(self,text):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 1px solid #2c2c2c;}"
                          "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.label = FontLabel(text, 10, False)
        self.waarde = FontLabel("0", 10, False)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.waarde, alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(self.layout) 

    def setWaarde(self, waarde):
        self.waarde.setText(waarde)

class VerlichtingSystemenDetectiesDetailsSet(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {padding : 10px; padding-left : 20px; padding-right : 20px; color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 1px solid #2c2c2c;}"
                          "FontLabel {color : #b2b2b2; background-color: #4c575b; border : 0px;}"
                          "QComboBox {padding-left : 10px; color : #b2b2b2; background-color: #4c575b; border : 1px solid black; border-radius : 2px;}"
                          "QComboBox:on  { background: #849296;}"
                          "QComboBox QAbstractItemView { padding : 0px; padding-left : 10px; border: 1px solid black; selection-background-color: #c6a64c; }"
                          "QPushButton {color : #b2b2b2; background-color: #4c575b; border : 1px solid black; border-radius : 2px;}"
                          "QPushButton::checked {color : #000000; background-color: #c6a64c; border : 1px solid black; border-radius : 2px;}")
        self.setAuto = QPushButton("Auto")
        self.setAuto.setCheckable(True)
        self.setStand = QComboBox()
        self.setAuto.setFixedWidth(40)
        self.setStandItems()       
        self.setLayout(self.layout)
        self.setAutoStand(True)

        self.layout.addWidget(self.setAuto, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.setStand)

    def setAutoStand(self, stand):
        self.setAuto.setChecked(stand)

    def setStandItems(self):
        self.setStand.addItem("0%")
        self.setStand.addItem("10%")
        self.setStand.addItem("20%")
        self.setStand.addItem("30%")
        self.setStand.addItem("40%")
        self.setStand.addItem("50%")
        self.setStand.addItem("60%")
        self.setStand.addItem("70%")
        self.setStand.addItem("80%")
        self.setStand.addItem("90%")
        self.setStand.addItem("100%")

class VerlichtingSystemenDetectiesDetails(SystemenDetectiesDetails):
    def __init__(self,text):
        super().__init__(text)
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.setters = VerlichtingSystemenDetectiesDetailsSet()
        self.niveau = SystemenDetectiesDetailsWaardeLabel("Niveau")
        self.capaciteit = SystemenDetectiesDetailsWaardeLabel("Capaciteit")
        self.energieverbruik = SystemenDetectiesDetailsWaardeLabel("Energieverbruik")
        self.branduren = SystemenDetectiesDetailsWaardeLabel("Branduren")
        self.branduren.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 2px solid black;}"
                                  "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.layout.addWidget(self.setters)
        self.layout.addWidget(self.niveau)
        self.layout.addWidget(self.capaciteit)
        self.layout.addWidget(self.energieverbruik)
        self.layout.addWidget(self.branduren)
        self.layout.addItem(self.verticalstrech)


class SlagboomSystemenDetectiesDetails(SystemenDetectiesDetails):
    def __init__(self,text):
        super().__init__(text)
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.state = SystemenDetectiesDetailsWaardeLabel("State")
        self.beschikbaarheid = SystemenDetectiesDetailsWaardeLabel("Beschikbaarheid")
        self.movement = SystemenDetectiesDetailsWaardeLabel("Movement")
        self.obstacle = SystemenDetectiesDetailsWaardeLabel("Obstacle")
        self.error = SystemenDetectiesDetailsWaardeLabel("Error")
        self.error.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 2px solid black;}"
                                  "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.layout.addWidget(self.state)
        self.layout.addWidget(self.beschikbaarheid)
        self.layout.addWidget(self.movement)
        self.layout.addWidget(self.obstacle)
        self.layout.addWidget(self.error)
        self.layout.addItem(self.verticalstrech)

class VerkeerslichtSystemenDetectiesDetails(SystemenDetectiesDetails):
    def __init__(self,text):
        super().__init__(text)
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.state = SystemenDetectiesDetailsWaardeLabel("State")
        self.beschikbaarheid = SystemenDetectiesDetailsWaardeLabel("Beschikbaarheid")
        self.error = SystemenDetectiesDetailsWaardeLabel("Error")
        self.error.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 2px solid black;}"
                                  "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.layout.addWidget(self.state)
        self.layout.addWidget(self.beschikbaarheid)
        self.layout.addWidget(self.error)
        self.layout.addItem(self.verticalstrech)

class SensorSystemenDetectiesDetails(SystemenDetectiesDetails):
    def __init__(self,text):
        super().__init__(text)
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.state = SystemenDetectiesDetailsWaardeLabel("State")
        self.CO = SystemenDetectiesDetailsWaardeLabel("CO")
        self.CO2 = SystemenDetectiesDetailsWaardeLabel("CO2")
        self.error = SystemenDetectiesDetailsWaardeLabel("Error")
        self.error.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 2px solid black;}"
                                  "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.layout.addWidget(self.state)
        self.layout.addWidget(self.CO)
        self.layout.addWidget(self.CO2)
        self.layout.addWidget(self.error)
        self.layout.addItem(self.verticalstrech)


class SystemenDetectieButton(QFrame):
    def __init__(self, text):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 1px solid #2c2c2c;}"
                           "QPushButton {color : #b2b2b2; background-color: #4c575b; border : 0px; text-align: left; padding-left : 70px}"
                           "QLabel {color : #b2b2b2; background-color: #4c575b; border : 0px; }")       
        self.setLayout(self.layout) 
        self.setMinimumHeight(20)
        self.button = QPushButton(text)
        self.button.setMinimumWidth(170)
        self.button.setMinimumHeight(20)
        font = QFont("Nirmala UI", 10)
        self.button.setFont(font)
        self.klVerkeerskundig = QLabel("")
        self.klVerkeerskundig.setFixedSize(20,20)
        self.Klhandmatig = QLabel("")
        self.Klhandmatig.setFixedSize(20,20)
        self.klKritisch = QLabel("")
        self.klKritisch.setFixedSize(20,20)
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.klVerkeerskundig)
        self.layout.addWidget(self.Klhandmatig)
        self.layout.addWidget(self.klKritisch)
        self.layout.addItem(self.horizontalSpacer)

    def setklVerkeerskundig(self):
        self.klVerkeerskundig.setPixmap(QIcon("icons/circle.svg").pixmap(15,15))

    def setKlhandmatig(self):
        self.Klhandmatig.setPixmap(QIcon("icons/square.svg").pixmap(15,15))

    def setklKritisch(self):
        self.klKritisch.setPixmap(QIcon("icons/triangle.svg").pixmap(15,15))
    
    def clearklVerkeerskundig(self):
        self.klVerkeerskundig.clear()

    def clearKlhandmatig(self):
        self.Klhandmatig.clear()

    def clearklKritisch(self):
        self.klKritisch.clear()    

class SystemenDetectiesFoldDetails(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #4c575b; border : 0px;}")       
        self.setLayout(self.layout) 

class SystemenDetectiesFoldDetailsBuis(SystemenDetectiesFoldDetails):
    def __init__(self):
        super().__init__()
        self.button_verlichting = SystemenDetectieButton("Verlichting")
        self.layout.addWidget(self.button_verlichting) 

class SystemenDetectiesFoldDetailsVerkeer(SystemenDetectiesFoldDetails):
    def __init__(self):
        super().__init__()
        self.button_slagboom = SystemenDetectieButton("Slagboom")
        self.button_verkeerslicht = SystemenDetectieButton("Verkeerslicht")
        self.layout.addWidget(self.button_slagboom)   
        self.layout.addWidget(self.button_verkeerslicht)

class SystemenDetectiesFoldDetailsSensoren(SystemenDetectiesFoldDetails):
    def __init__(self):
        super().__init__()
        self.button_sensor1 = SystemenDetectieButton("Luchtsensor")
        self.layout.addWidget(self.button_sensor1)   

class SystemenDetectieFoldButton(QFrame):
    def __init__(self, text):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #4c575b; border : 0px; border-bottom : 1px solid #000000;border-top : 2px solid #000000; border-radius: 0px;}"
                           "QPushButton {color : #b2b2b2; background-color: #4c575b; text-align: left; border : 0px;}"
                           "QLabel {color : #b2b2b2; background-color: #4c575b; border: 0px; }"
                           )
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setMinimumHeight(24)
        self.button = QPushButton(text)
        self.button.setIcon(QIcon("icons/caret-right.svg"))
        self.button.setMinimumWidth(100)
        font = QFont("Nirmala UI", 10)
        font.setBold(True)
        self.button.setFont(font)
        self.klVerkeerskundig = QLabel("")
        self.klVerkeerskundig.setFixedSize(20,20)
        self.Klhandmatig = QLabel("")
        self.Klhandmatig.setFixedSize(20,20)
        self.klKritisch = QLabel("")
        self.klKritisch.setFixedSize(20,20)
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.klVerkeerskundig)
        self.layout.addWidget(self.Klhandmatig)
        self.layout.addWidget(self.klKritisch)
        self.layout.addItem(self.horizontalSpacer)
        self.folded = True

    def setklVerkeerskundig(self):
        self.klVerkeerskundig.setPixmap(QIcon("icons/circle.svg").pixmap(15,15))

    def setKlhandmatig(self):
        self.Klhandmatig.setPixmap(QIcon("icons/square.svg").pixmap(15,15))

    def setklKritisch(self):
        self.klKritisch.setPixmap(QIcon("icons/triangle.svg").pixmap(15,15))
    
    def clearklVerkeerskundig(self):
        self.klVerkeerskundig.clear()

    def clearKlhandmatig(self):
        self.Klhandmatig.clear()

    def clearklKritisch(self):
        self.klKritisch.clear()  


class SystemenDetectiesList(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10,4,10,4)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setFixedWidth(275)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-right: 1px solid black; border-left: 1px solid black;border-radius : 0px}")
        self.fold_button_buis = SystemenDetectieFoldButton("Buis")
        self.fold_button_buis.button.clicked.connect(self.buisActive)        
        self.fold_details_buis = SystemenDetectiesFoldDetailsBuis()
        self.fold_button_verkeer= SystemenDetectieFoldButton("Verkeer")
        self.fold_button_verkeer.button.clicked.connect(self.verkeerActive)
        self.fold_details_verkeer = SystemenDetectiesFoldDetailsVerkeer()
        self.fold_button_sensoren= SystemenDetectieFoldButton("Sensoren")
        self.fold_button_sensoren.button.clicked.connect(self.sensorenActive)
        self.fold_details_sensoren = SystemenDetectiesFoldDetailsSensoren()        
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        #self.layout.addWidget(self.fold_button_buis)
        #self.layout.addWidget(self.fold_details_buis)
        self.layout.addWidget(self.fold_button_verkeer)
        self.layout.addWidget(self.fold_details_verkeer)
        self.layout.addWidget(self.fold_button_sensoren)
        self.layout.addWidget(self.fold_details_sensoren)
        self.layout.addItem(self.verticalstrech)

        self.fold_details_buis.hide()
        self.fold_details_verkeer.hide()
        self.fold_details_sensoren.hide()

    def buisActive(self):
        if self.fold_button_buis.folded:
            self.fold_button_buis.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_buis.folded = False
            self.fold_details_buis.show()
        else:
            self.fold_button_buis.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_buis.folded = True
            self.fold_details_buis.hide()

    def verkeerActive(self):
        if self.fold_button_verkeer.folded:
            self.fold_button_verkeer.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_verkeer.folded = False
            self.fold_details_verkeer.show()
        else:
            self.fold_button_verkeer.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_verkeer.folded = True
            self.fold_details_verkeer.hide()

    def sensorenActive(self):
        if self.fold_button_sensoren.folded:
            self.fold_button_sensoren.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_sensoren.folded = False
            self.fold_details_sensoren.show()
        else:
            self.fold_button_sensoren.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_sensoren.folded = True
            self.fold_details_sensoren.hide()

class SystemenDetectiesFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10,10,10,10)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setStyleSheet("SystemenDetectiesFrame {color : #b2b2b2; background-color: #30393c; border-radius: 5px;}")
        self.horizontalstretch = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.systemen_detecties_list = SystemenDetectiesList()
        self.verlichting_details = VerlichtingSystemenDetectiesDetails("Verlichting")
        self.slagboom_details = SlagboomSystemenDetectiesDetails("Slagboom")
        self.verkeerslicht_details = VerkeerslichtSystemenDetectiesDetails("Verkeerslicht")
        self.sensor1_details = SensorSystemenDetectiesDetails("Luchtsensor")

        self.layout.addWidget(self.systemen_detecties_list)
        #self.layout.addWidget(self.verlichting_details)
        self.layout.addWidget(self.slagboom_details)
        self.layout.addWidget(self.verkeerslicht_details)
        self.layout.addWidget(self.sensor1_details)
        self.layout.addItem(self.horizontalstretch)



class SystemenDetecties(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10,0,10,0)
        self.setStyleSheet("color : #b2b2b2; background-color: #30393c; border: 1px solid black; border-radius: 5px;")

        self.setStyleSheet( "QTabBar:tab {height : 120px; width : 30px; color : #b2b2b2; background-color: #30393c; border-radius: 2px; font-size: 16px; border-top-left-radius: 5px;border-bottom-left-radius: 5px;}"
                            "QTabBar:tab:selected {color : #b2b2b2; background-color: #4c575b;}"
                            "QTabWidget::pane { border: 1px}")
        self.setTabPosition(QTabWidget.TabPosition.West)
        self.setTabIcon(1, QIcon("icons/square.svg"))
        self.setMaximumWidth(600)
        self.rijbaan1 = SystemenDetectiesFrame()

        self.addTab(self.rijbaan1, "Rijbaan 1")

        self.standard_stylesheet = "QFrame {color : #b2b2b2; background-color: #4c575b; border : 0px;border-bottom : 1px solid #2c2c2c;} QPushButton {color : #b2b2b2; background-color: #4c575b; border : 0px; text-align: left; padding-left : 70px} QLabel {color : #b2b2b2; background-color: #4c575b; border : 0px; }"
        self.clicked_stylesheet = "QFrame {color : #000000; background-color: #c6a64c; border : 0px;border-bottom : 1px solid #2c2c2c;} QPushButton {color : #000000; background-color: #c6a64c; border : 0px; text-align: left; padding-left : 70px} QLabel {color : #000000; background-color: #c6a64c; border : 0px; }"
        self.connectButtons()
        self.hideDetails()

    def connectButtons(self):
        self.rijbaan1.systemen_detecties_list.fold_details_buis.button_verlichting.button.clicked.connect(self.verlichtingActive)
        self.rijbaan1.systemen_detecties_list.fold_details_verkeer.button_slagboom.button.clicked.connect(self.slagboomActive)
        self.rijbaan1.systemen_detecties_list.fold_details_verkeer.button_verkeerslicht.button.clicked.connect(self.verkeerslichtActive)
        self.rijbaan1.systemen_detecties_list.fold_details_sensoren.button_sensor1.button.clicked.connect(self.sensor1Active)

    
    def hideDetails(self):
        self.rijbaan1.verlichting_details.hide()
        self.rijbaan1.slagboom_details.hide()
        self.rijbaan1.verkeerslicht_details.hide()
        self.rijbaan1.sensor1_details.hide()

        self.rijbaan1.systemen_detecties_list.fold_details_buis.button_verlichting.setStyleSheet(self.standard_stylesheet)
        self.rijbaan1.systemen_detecties_list.fold_details_verkeer.button_slagboom.setStyleSheet(self.standard_stylesheet)
        self.rijbaan1.systemen_detecties_list.fold_details_verkeer.button_verkeerslicht.setStyleSheet(self.standard_stylesheet)
        self.rijbaan1.systemen_detecties_list.fold_details_sensoren.button_sensor1.setStyleSheet(self.standard_stylesheet)



    def verlichtingActive(self):
        self.hideDetails()
        if self.rijbaan1.verlichting_details.isVisible() == False:
            self.rijbaan1.verlichting_details.show()
            self.rijbaan1.systemen_detecties_list.fold_details_buis.button_verlichting.setStyleSheet(self.clicked_stylesheet)   

    def slagboomActive(self):
        self.hideDetails()
        if self.rijbaan1.slagboom_details.isVisible() == False:
            self.rijbaan1.slagboom_details.show()
            self.rijbaan1.systemen_detecties_list.fold_details_verkeer.button_slagboom.setStyleSheet(self.clicked_stylesheet) 

    def verkeerslichtActive(self):
        self.hideDetails()
        if self.rijbaan1.verkeerslicht_details.isVisible() == False:
            self.rijbaan1.verkeerslicht_details.show()
            self.rijbaan1.systemen_detecties_list.fold_details_verkeer.button_verkeerslicht.setStyleSheet(self.clicked_stylesheet)  


    def sensor1Active(self):
        self.hideDetails()
        if self.rijbaan1.sensor1_details.isVisible() == False:
            self.rijbaan1.sensor1_details.show()
            self.rijbaan1.systemen_detecties_list.fold_details_sensoren.button_sensor1.setStyleSheet(self.clicked_stylesheet) 
        

        