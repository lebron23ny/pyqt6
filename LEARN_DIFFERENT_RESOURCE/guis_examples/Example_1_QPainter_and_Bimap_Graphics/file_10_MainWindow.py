import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt


from file_10_User_Widgets import Canvas, QPaletteButton, COLORS

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()
        self.setFixedSize(600, 300)

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)



        palatte = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palatte)
        l.addLayout(palatte)
        self.setCentralWidget(w)


    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()