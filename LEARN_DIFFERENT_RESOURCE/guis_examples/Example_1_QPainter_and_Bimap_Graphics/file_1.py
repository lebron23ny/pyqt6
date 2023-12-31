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
        painter = QtGui.QPainter(self.label.pixmap())


        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)

        painter.drawLine(10, 10, 300, 200)
        painter.drawPoint(200, 150)
        painter.end()



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
