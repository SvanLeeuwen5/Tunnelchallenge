from PyQt6.QtWidgets import QVBoxLayout, QFrame, QPushButton, QLineEdit, QSpacerItem, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
from font import FontLabel

class LoginFrame(QFrame):

    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #000000;}")
        self.setContentsMargins(10,10,10,10)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.addFrames()    

    def addFrames(self):
        self.verticalstrech1 = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.verticalstrech2 = QSpacerItem(0,0,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        self.login_frame = QFrame()

        self.layout.addItem(self.verticalstrech1)
        self.layout.addWidget(self.login_frame, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addItem(self.verticalstrech2)
        self.login_frame.setMaximumWidth(600)
        self.login_frame.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border-radius: 10px;}")
        self.login_frame.setContentsMargins(10,10,10,10)
        self.login_layout = QGridLayout()
        self.login_frame.setLayout(self.login_layout)

        dashboard_label = FontLabel('Tunnel controle', 20, True)
        username_label = FontLabel('Gebruiker:', 12, False)
        self.user_status = FontLabel(' ', 12, False)
        password_label = FontLabel('Wachtwoord:', 12, False)   
        self.password_status = FontLabel(' ', 12, False) 
        self.password_status.setStyleSheet("QLabel {color : #aa1d1d;}")
        self.user_status.setStyleSheet("QLabel {color : #aa1d1d;}")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Gebruiker')
        self.password_input = QLineEdit()  
        self.password_input.setPlaceholderText('Wachtwoord')
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)        
        self.login_button = QPushButton('Inloggen')

        self.login_button.clicked.connect(self.checkLogin)

        self.login_layout.addWidget(dashboard_label, 0,1,1,3,Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(username_label, 1,1,1,6,Qt.AlignmentFlag.AlignLeft)
        self.login_layout.addWidget(self.username_input,2,1,1,6)
        self.login_layout.addWidget(self.user_status,3,1,1,6,Qt.AlignmentFlag.AlignLeft)
        self.login_layout.addWidget(password_label,4,1,1,6,Qt.AlignmentFlag.AlignLeft)
        self.login_layout.addWidget(self.password_input,5,1,1,6)
        self.login_layout.addWidget(self.password_status,6,1,1,6,Qt.AlignmentFlag.AlignLeft)
        self.login_layout.addWidget(self.login_button,7,5,1,2,Qt.AlignmentFlag.AlignRight)

    def checkLogin(self):
        self.password_status.setText('')
        self.user_status.setText('')
        if self.username_input.text() == 'user':
            if self.password_input.text() == 'user':
                self.parent.menu.show()
                self.parent.dashboardActive()
                self.username_input.setText('')
                self.password_input.setText('')
            else:
                self.password_status.setText('Verkeerde wachtwoord')
        else:
            self.user_status.setText('Gebruiker niet gevonden')