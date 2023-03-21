from PyQt6.QtWidgets import  QFrame, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QLabel
from PyQt6.QtCore import QMargins, Qt, QSize, QEvent
from PyQt6.QtGui import QIcon, QFont, QPixmap


class MenuButton(QPushButton):
    def __init__(self, text, icon):
        super().__init__()
        self.button_icon = icon
        self.setCheckable(True)
        self.setFixedHeight(50)
        self.setIconSize(QSize(30,30)) 
        self.setStyleSheet("""QPushButton {color : #afafaf; background-color: #3c3c3c; border : none }""")
        self.setIcon(QIcon(self.button_icon+".svg"))	  
        self.active = False   
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def event(self, e: QEvent) -> bool:
        if e.type() == QEvent.Type.HoverEnter:
            if self.active == False:
                self.setIcon(QIcon(self.button_icon+"_hover.svg"))
                self.setStyleSheet("QPushButton {color : #0078d7; background-color: #3c3c3c; border : none }")	
        if e.type() == QEvent.Type.HoverLeave: 
            if self.active == False:   
                self.setIcon(QIcon(self.button_icon+".svg"))
                self.setStyleSheet("QPushButton {color : #afafaf; background-color: #3c3c3c; border : none }")	    
        return super().event(e)    

    def contentActive(self, bool):
        if bool:
            self.active = True
            self.setIcon(QIcon(self.button_icon+"_hover.svg"))
            self.setStyleSheet("QPushButton { border-left : 3px solid  #0078d7; margin-right : 3px ;}")
        else:
            self.active = False
            self.setStyleSheet("QPushButton { }")
            self.setIcon(QIcon(self.button_icon+".svg"))

class Menu(QFrame):
    def __init__(self, parent):
        super(Menu, self).__init__(parent)
        self.parent = parent
        self.createLayout()
        self.createButtons()
        self.setStyleSheet("color : #afafaf; background-color: #3c3c3c;border : none ")
      

    def createLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setFixedWidth(50)
        self.layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.layout.setSpacing(0)    

    def createButtons(self):
        self.user_icon = QLabel()
        user_pixmap = QPixmap("./icons/user.svg").scaled(30,30,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation)
        self.user_icon.setPixmap(user_pixmap)
        self.user_icon.setFixedHeight(50)
        self.user_name = QLabel("WVL")
        self.verticalstrech1 = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.button_dashboard = MenuButton("Dashboard", "icons\monitor")
        self.button_camera = MenuButton("Camera", "icons\\video")
        self.verticalstrech2 = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)

        self.button_logout = MenuButton("Uitloggen", "icons\log-out")


        self.layout.addWidget(self.user_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.user_name, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addItem(self.verticalstrech1)
        self.layout.addWidget(self.button_dashboard)
        self.layout.addWidget(self.button_camera)
        self.layout.addItem(self.verticalstrech2)
        self.layout.addWidget(self.button_logout)
