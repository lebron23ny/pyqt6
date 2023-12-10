#https://www.pythonguis.com/tutorials/bitmap-graphics/

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        from random import randint
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)
        # painter.drawRect(50, 50, 100, 100)
        # painter.drawRect(60, 60, 150, 100)
        # painter.drawRect(70, 70, 100, 150)
        # painter.drawRect(80, 80, 150, 100)
        # painter.drawRect(90, 90, 100, 150)
        painter.drawRects(
            QtCore.QRect(50, 50, 100, 100),
            QtCore.QRect(60, 60, 150, 100),
            QtCore.QRect(70, 70, 100, 150),
            QtCore.QRect(80, 80, 150, 100),
            QtCore.QRect(90, 90, 100, 150),
        )
        painter.end()



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
