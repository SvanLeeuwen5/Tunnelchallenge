from PyQt6.QtWidgets import QGridLayout, QFrame, QPushButton, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QTabWidget, QHBoxLayout, QApplication, QWidget, QTableView, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QGroupBox, QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from font import FontLabel

class MeldingLijstTableFrame(QFrame):
    def __init__(self):
        super().__init__()
        table_layout = QVBoxLayout()
        self.setLayout(table_layout)

        self.table = QTableWidget()
        self.setStyleSheet( "QTableView {color : #b2b2b2; background-color: #4c575b;}"
                            "QHeaderView::section {color : #b2b2b2; background-color: #4c575b;}"
                            "QHeaderView::section:horizontal {color : #b2b2b2; background-color: #4c575b;}")

        self.table.setRowCount(50)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Type", "Cam ", "Tijdstip", "Locatie", "Melding", "Ond", "Notitie"])
        
        horizontal_header = QHeaderView(Qt.Orientation.Horizontal)
        self.table.setHorizontalHeader(horizontal_header)
        self.table.verticalHeader().hide()
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        horizontal_header.setStretchLastSection(True)

        # Data aan tabel toevoegen (random bijgedaan)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(f"Row {i}, Col {j}"))



        table_layout.addWidget(self.table)

        



class MeldingLijstButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("QPushButton {color : #b2b2b2; background-color: #4c575b; border : 1px solid black; border-radius: 5px;}")
        self.setFixedSize(30,30)
        self.setIcon(QIcon("icons/check.svg"))


class MeldingLijstButtonFrame(QFrame):
    def __init__(self):
        super().__init__()
        # Create buttons for the table frame
        self.horizontalSpacer = QSpacerItem(0,0,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        button_layout = QHBoxLayout()
        self.setLayout(button_layout)
        meldinglijst_label = FontLabel("Onbevestigde meldingen",14, True)
        button_layout.addWidget(meldinglijst_label, alignment=Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)
        button_layout.addItem(self.horizontalSpacer)
        for i in range(7):
            button = MeldingLijstButton("")
            button_layout.addWidget(button)


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