from PyQt6.QtWidgets import QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout
from PyQt6.QtGui import QIcon

class SystemenDetectiesDetails(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)    
        self.setMinimumWidth(300)

class SystemenDetectieButton(QFrame):
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
        self.icon1.setPixmap(QIcon("icons/circle.svg").pixmap(15,15))
        self.icon1.setFixedSize(20,20)
        self.icon2 = QLabel("")
        self.icon2.setPixmap(QIcon("icons/square.svg").pixmap(15,15))
        self.icon2.setFixedSize(20,20)
        self.icon3 = QLabel("")
        self.icon3.setPixmap(QIcon("icons/triangle.svg").pixmap(15,15))
        self.icon3.setFixedSize(20,20)
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.icon1)
        self.layout.addWidget(self.icon2)
        self.layout.addWidget(self.icon3)
        self.layout.addItem(self.horizontalSpacer)

class SystemenDetectiesFoldDetails(QFrame):
    def __init__(self, list):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0) 
        self.setStyleSheet("QFrame {color : #000000; background-color: #4c575b; border : 0px;}")       
        self.setLayout(self.layout) 
        for name in list:
            self.layout.addWidget(SystemenDetectieButton(name)) 


class SystemenDetectieFoldButton(QFrame):
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
        self.button.setIcon(QIcon("icons/caret-right.svg"))
        self.button.setMinimumWidth(100)
        self.icon1 = QLabel("")
        self.icon1.setPixmap(QIcon("icons/circle.svg").pixmap(15,15))
        self.icon1.setFixedSize(20,20)
        self.icon2 = QLabel("")
        self.icon2.setPixmap(QIcon("icons/square.svg").pixmap(15,15))
        self.icon2.setFixedSize(20,20)
        self.icon3 = QLabel("")
        self.icon3.setPixmap(QIcon("icons/triangle.svg").pixmap(15,15))
        self.icon3.setFixedSize(20,20)
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.icon1)
        self.layout.addWidget(self.icon2)
        self.layout.addWidget(self.icon3)
        self.layout.addItem(self.horizontalSpacer)

        self.folded = True


class SystemenDetectiesList(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(4,4,4,4)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setFixedWidth(300)
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-right: 1px solid black; border-left: 1px solid black;border-radius : 0px}")
        self.fold_button_buis = SystemenDetectieFoldButton("Buis")
        self.fold_button_buis.button.clicked.connect(self.buisActive)        
        self.fold_details_buis = SystemenDetectiesFoldDetails({"Ventilatie", "Verlichting", "CCTV"})
        self.fold_button_vluchtweg = SystemenDetectieFoldButton("Vluchtweg")
        self.fold_button_vluchtweg.button.clicked.connect(self.vluchtwegActive)
        self.fold_details_vluchtweg = SystemenDetectiesFoldDetails({"Vluchtdeur"})
        self.fold_button_tunnel = SystemenDetectieFoldButton("Tunnel")
        self.fold_button_tunnel.button.clicked.connect(self.tunnelActive)
        self.fold_details_tunnel = SystemenDetectiesFoldDetails({"Blusvoorziening","Vloeistofafvoer"})
        self.fold_button_verkeer = SystemenDetectieFoldButton("Verkeer")
        self.fold_button_verkeer.button.clicked.connect(self.verkeerActive)
        self.fold_details_verkeer = SystemenDetectiesFoldDetails({"Verkeer", "Verkeer", "Verkeer"})
        self.fold_button_detecties= SystemenDetectieFoldButton("Detecties")

        self.verticalstrech = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        self.layout.addWidget(self.fold_button_buis)
        self.layout.addWidget(self.fold_details_buis)
        self.layout.addWidget(self.fold_button_vluchtweg)
        self.layout.addWidget(self.fold_details_vluchtweg)
        self.layout.addWidget(self.fold_button_tunnel)
        self.layout.addWidget(self.fold_details_tunnel)
        self.layout.addWidget(self.fold_button_verkeer)
        self.layout.addWidget(self.fold_details_verkeer)
        self.layout.addWidget(self.fold_button_detecties)
        self.layout.addItem(self.verticalstrech)

        self.fold_details_buis.hide()
        self.fold_details_vluchtweg.hide()
        self.fold_details_tunnel.hide()
        self.fold_details_verkeer.hide()

    def buisActive(self):
        if self.fold_button_buis.folded:
            self.fold_button_buis.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_buis.folded = False
            self.fold_details_buis.show()
        else:
            self.fold_button_buis.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_buis.folded = True
            self.fold_details_buis.hide()

    def vluchtwegActive(self):
        if self.fold_button_vluchtweg.folded:
            self.fold_button_vluchtweg.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_vluchtweg.folded = False
            self.fold_details_vluchtweg.show()
        else:
            self.fold_button_vluchtweg.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_vluchtweg.folded = True
            self.fold_details_vluchtweg.hide()        

    def tunnelActive(self):
        if self.fold_button_tunnel.folded:
            self.fold_button_tunnel.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_tunnel.folded = False
            self.fold_details_tunnel.show()
        else:
            self.fold_button_tunnel.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_tunnel.folded = True
            self.fold_details_tunnel.hide()

    def verkeerActive(self):
        if self.fold_button_verkeer.folded:
            self.fold_button_verkeer.button.setIcon(QIcon("icons/caret-down.svg"))
            self.fold_button_verkeer.folded = False
            self.fold_details_verkeer.show()
        else:
            self.fold_button_verkeer.button.setIcon(QIcon("icons/caret-right.svg"))
            self.fold_button_verkeer.folded = True
            self.fold_details_verkeer.hide()

class SystemenDetectiesFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10,10,10,10)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.setStyleSheet("SystemenDetectiesFrame {color : #b2b2b2; background-color: #30393c; border-radius: 5px;}")
        self.horizontalstretch = QSpacerItem(300,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        
        self.systemen_detecties_list = SystemenDetectiesList()
        self.layout.addWidget(self.systemen_detecties_list)
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
        self.setFixedWidth(600)
        self.re_frame = SystemenDetectiesFrame()
        self.wi_frame  = SystemenDetectiesFrame()
        self.h_li_frame = SystemenDetectiesFrame()
        self.p_li_frame = SystemenDetectiesFrame()
        self.addTab(self.re_frame, "Rijbaan 1")
        self.addTab(self.wi_frame, "Rijbaan 2")
        self.addTab(self.h_li_frame, "Rijbaan 3")
        self.addTab(self.p_li_frame, "Rijbaan 4")