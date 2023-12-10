import os
import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


class ql(QLineEdit):
    def __init__(self, wg):
       self.wg = wg
       super().__init__(wg)
       self.move(20, 20)
       self.resize(500, 28)
       self.setFocus()

    def keyPressEvent(self, e):
# отработать символ внутри поля ввода
       k = e.key()
       super().keyPressEvent(e)
       print("QLineEdit:",k)

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 100)
        self.setWindowTitle('Обработка клавиш клавиатуры')
        self.name_input = ql(self)

    def keyPressEvent(self, e):
        print("QWidget:",e.key())


app = QApplication(sys.argv)
ex = Win()
ex.show()
sys.exit(app.exec())