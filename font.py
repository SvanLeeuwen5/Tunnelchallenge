from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont

class FontLabel(QLabel):
    def __init__(self, text:str, size:int, bold:bool):
        super().__init__(text)
        font = QFont("Nirmala UI", size)
        font.setBold(bold)
        self.setFont(font)  
        self.setStyleSheet("QLabel {color : #b2b2b2; background-color: #2c2c2c; border : none}")
        