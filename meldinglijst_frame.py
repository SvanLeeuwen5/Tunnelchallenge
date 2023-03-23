from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout, QApplication, QWidget, QTableView, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QGroupBox, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from font import FontLabel

class MeldingLijstTableFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.itemCount = 0
        table_layout = QVBoxLayout()
        self.setLayout(table_layout)

        self.table = QTableWidget()
        self.setStyleSheet( "QTableView {color : #b2b2b2; background-color: #4c575b;}"
                            "QHeaderView::section {color : #b2b2b2; background-color: #4c575b;}"
                            "QHeaderView::section:horizontal {color : #b2b2b2; background-color: #4c575b;}")

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Type", "Cam ", "Tijdstip", "Locatie", "Melding", "Ond", "Notitie"])
        
        horizontal_header = QHeaderView(Qt.Orientation.Horizontal)
        self.table.setHorizontalHeader(horizontal_header)
        self.table.verticalHeader().hide()
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        horizontal_header.setStretchLastSection(True)

        self.newItem()
        self.newItem()
        self.newItem()
        table_layout.addWidget(self.table)

    def newItem(self):
        self.table.insertRow(0)
        for j in range(self.table.columnCount()):
            item = QTableWidgetItem(f"Row {self.itemCount}, Col {j}")
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(0, j, item)
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