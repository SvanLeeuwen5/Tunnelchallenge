from PyQt6.QtWidgets import QFrame, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout,QHBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from font import FontLabel

#refactor the following class

class MeldingLijstTableItem(QTableWidgetItem):
    def __init__(self, text):
        super(MeldingLijstTableItem, self).__init__(text)
        self.setFlags(self.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        if text == "square":
            self.setText("")
            self.setIcon(QIcon('icons/square.svg'))
        if text == "triangle":
            self.setText("")
            self.setIcon(QIcon('icons/triangle.svg'))
        if text == "circle":
            self.setText("")
            self.setIcon(QIcon('icons/circle.svg'))
          
class MeldingLijstTableTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(7)
        self.setHorizontalHeaderLabels(["Type", "Cam ", "Tijdstip", "Locatie", "Melding", "Ond", "Notitie"])
        horizontal_header = QHeaderView(Qt.Orientation.Horizontal)
        self.setHorizontalHeader(horizontal_header)
        self.verticalHeader().hide()
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        horizontal_header.setStretchLastSection(True)

class MeldingLijstTableFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.itemCount = 0
        table_layout = QVBoxLayout()
        self.setLayout(table_layout)
        self.table = MeldingLijstTableTable()
        self.setStyleSheet( "QTableView {color : #b2b2b2; background-color: #4c575b;}"
                            "QHeaderView::section {color : #b2b2b2; background-color: #4c575b;}"
                            "QHeaderView::section:horizontal {color : #b2b2b2; background-color: #4c575b;}")

        self.newItem("circle", "18", "28-10-11 16:11:00", "Rijbaan 1", "SOS", "", "")
        self.newItem("triangle", "18", "28-10-11 16:11:00", "Rijbaan 1", "SOS", "", "")
        self.newItem("square", "18", "28-10-11 16:11:00", "Rijbaan 1", "SOS", "", "")
        table_layout.addWidget(self.table)

    #TODO Add a new item to the table with actual data

    def newItem(self, type, cam , tijdstip, locatie, melding, ond, notitie):
        self.table.insertRow(0)
        item = MeldingLijstTableItem(type)

        self.table.setItem(0, 0, item)
        item = MeldingLijstTableItem(cam)
        self.table.setItem(0, 1, item)
        item = MeldingLijstTableItem(tijdstip)
        self.table.setItem(0, 2, item)
        item = MeldingLijstTableItem(locatie)
        self.table.setItem(0, 3, item)
        item = MeldingLijstTableItem(melding)
        self.table.setItem(0, 4, item)
        item = MeldingLijstTableItem(ond)
        self.table.setItem(0, 5, item)
        item = MeldingLijstTableItem(notitie)
        self.table.setItem(0, 6, item)
        self.itemCount += 1

    def removeItem(self):
        self.itemCount -= 1
        self.table.removeRow(0)

    def removeAllItems(self):
        for i in range(self.itemCount):
            self.table.removeRow(0)
        self.itemCount = 0


class MeldingLijstButton(QPushButton):
    def __init__(self, text, icon):
        super().__init__(text)
        self.setStyleSheet("QPushButton {color : #b2b2b2; background-color: #4c575b; border : 1px solid black; border-radius: 5px;}")
        self.setFixedSize(30,30)
        self.setIcon(QIcon(icon))


class MeldingLijstButtonFrame(QFrame):
    def __init__(self):
        super().__init__()
        # Create buttons for the table frame
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        button_layout = QHBoxLayout()
        self.setLayout(button_layout)
        meldinglijst_label = FontLabel("Onbevestigde meldingen",14, True)

        self.button_check = MeldingLijstButton("","icons/check.svg")
        self.button_check_all = MeldingLijstButton("","icons/check-double.svg")
        

        button_layout.addWidget(meldinglijst_label, alignment=Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)
        button_layout.addItem(self.horizontalSpacer)
        button_layout.addWidget(self.button_check)
        button_layout.addWidget(self.button_check_all)


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

        self.buttons.button_check.clicked.connect(self.tabel_lijst.removeItem)
        self.buttons.button_check_all.clicked.connect(self.tabel_lijst.removeAllItems)

        self.layout.addWidget(self.buttons)
        self.layout.addWidget(self.tabel_lijst)