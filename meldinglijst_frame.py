from PyQt6.QtWidgets import QFrame, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout,QHBoxLayout, QComboBox
from PyQt6.QtCore import Qt
from font import FontLabel

class SystemenDetectiesDetailsWaardeLabel(QFrame):
    def __init__(self,text):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px; border-radius : 0px; border-bottom : 1px solid #2c2c2c;}"
                          "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px; border-radius : 0px}")
        self.label = FontLabel(text, 10, False)
        self.waarde = FontLabel("0", 10, False)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.waarde, alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(self.layout) 

    def setWaarde(self, waarde):
        self.waarde.setText(str(waarde))

class VerlichtingSystemenDetectiesDetailsSet(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {padding : 10px; padding-left : 20px; padding-right : 20px; color : #b2b2b2; background-color: #4c575b; border : 0px; border-radius : 0px; border-bottom : 1px solid #2c2c2c;}"
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

class VerlichtingFrame(QFrame):
    def __init__(self, text):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10,4,10,4)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)  
        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.label = FontLabel(text, 12, True)
        self.label.setStyleSheet("FontLabel {padding : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px; border-radius : 4px; border-bottom : 2px solid black;}")
        self.setters = VerlichtingSystemenDetectiesDetailsSet()
        self.niveau = SystemenDetectiesDetailsWaardeLabel("Niveau")
        self.capaciteit = SystemenDetectiesDetailsWaardeLabel("Capaciteit")
        self.energieverbruik = SystemenDetectiesDetailsWaardeLabel("Energieverbruik")
        self.branduren = SystemenDetectiesDetailsWaardeLabel("Branduren")
        self.branduren.setStyleSheet("QFrame {padding-left : 10px; padding-right : 10px; color : #b2b2b2; background-color: #4c575b; border : 0px;}"
                                  "FontLabel {padding : 2px; color : #b2b2b2; background-color: #4c575b; border : 0px;}")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.setters)
        self.layout.addWidget(self.niveau)
        self.layout.addWidget(self.capaciteit)
        self.layout.addWidget(self.energieverbruik)
        self.layout.addWidget(self.branduren)
        self.layout.addItem(self.verticalstrech)

class MeldingLijstTableFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.itemCount = 0
        table_layout = QHBoxLayout()
        self.setLayout(table_layout)
        self.setContentsMargins(0,0,0,0)
        table_layout.setSpacing(0)
        table_layout.setContentsMargins(0,0,0,0)
        self.setStyleSheet("QFrame {border-radius : 0px; border-bottom-right-radius : 4px;border-bottom-left-radius : 4px;}")

        self.verlichting1 = VerlichtingFrame("Lamp 1")
        self.verlichting2 = VerlichtingFrame("Lamp 2")
        self.verlichting3 = VerlichtingFrame("Lamp 3")
        self.verlichting4 = VerlichtingFrame("Lamp 4")
        self.verlichting5 = VerlichtingFrame("Lamp 5")

        table_layout.addWidget(self.verlichting1)
        table_layout.addWidget(self.verlichting2)
        table_layout.addWidget(self.verlichting3)
        table_layout.addWidget(self.verlichting4)
        table_layout.addWidget(self.verlichting5)

class MeldingLijstButtonFrame(QFrame):
    def __init__(self):
        super().__init__()
        # Create buttons for the table frame
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        button_layout = QHBoxLayout()
        self.setLayout(button_layout)
        meldinglijst_label = FontLabel("Verlichting",14, True)
        self.setStyleSheet("FontLabel {padding : 4px; border-bottom: 1px solid white;border-radius: 0px;}")

        button_layout.addWidget(meldinglijst_label)#, alignment=Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)
        #button_layout.addItem(self.horizontalSpacer)


class MeldingLijst(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)  
        self.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-radius: 5px;}")  
        
        self.tabel_lijst = MeldingLijstTableFrame()
        self.buttons = MeldingLijstButtonFrame()

        self.layout.addWidget(self.buttons)
        self.layout.addWidget(self.tabel_lijst)