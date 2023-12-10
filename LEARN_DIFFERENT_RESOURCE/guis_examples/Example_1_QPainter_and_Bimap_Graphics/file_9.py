#https://www.pythonguis.com/tutorials/bitmap-graphics/

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(600, 400)
        canvas.fill(QtGui.QColor(255, 255, 255))
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.last_x, self.last_y = None, None


    # def mousePressEvent(self, e):
    #     if self.last_x is None:
    #         self.last_x = e.x()
    #         self.last_y = e.y()
    #         return
    #     if e.button() == Qt.MouseButton.MiddleButton:
    #         self.last_x = None
    #         self.last_y = None
    #         return
    #
    #     painter = QtGui.QPainter(self.label.pixmap())
    #     painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
    #     painter.end()
    #     self.update()
    #     self.last_x = e.x()
    #     self.last_y = e.y()


    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return


        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def draw_something(self):
        from random import randint
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204, 0, 0))  # r, g, b
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, 'Hello, world!')
        painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
