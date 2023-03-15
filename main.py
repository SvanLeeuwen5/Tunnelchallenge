from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("QMainWindow")
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Click me!"))
    window.setLayout(layout)
    window.show()
    app.exec()

if __name__ == '__main__':
    main()