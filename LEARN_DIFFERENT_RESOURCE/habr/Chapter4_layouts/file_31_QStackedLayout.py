#https://habr.com/ru/companies/skillfactory/articles/648845/

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, \
    QLabel, QLineEdit, QListWidget
from PyQt6.QtWidgets import QStackedLayout
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class SubWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout_sub_widget = QVBoxLayout()
        self.setLayout(layout_sub_widget)
        label_sub = QLabel('Label 1')
        textEdit_sub = QLineEdit()
        listWidget_sub = QListWidget()
        listWidget_sub.addItem('ПН')
        listWidget_sub.addItem('ВТ')
        listWidget_sub.addItem('СР')
        listWidget_sub.addItem('ЧТ')
        listWidget_sub.addItem('ПТ')
        listWidget_sub.addItem('СБ')
        listWidget_sub.addItem('ВС')
        button_sub = QPushButton('Click')
        layout_sub_widget.addWidget(label_sub)
        layout_sub_widget.addWidget(textEdit_sub)
        layout_sub_widget.addWidget(listWidget_sub)
        layout_sub_widget.addWidget(button_sub)
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()




        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        btn = QPushButton("Custom Widget")
        btn.pressed.connect(self.activate_tab_4)
        button_layout.addWidget(btn)
        custom_widget = SubWidget()
        self.stacklayout.addWidget(custom_widget)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()