import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QSizePolicy
import random


SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10

class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        #pixmap.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        # if self.last_x is None: # First event.
        #     self.last_x = e.x()
        #     self.last_y = e.y()
        #     return # Ignore the first time.
        #
        # painter = QtGui.QPainter(self.pixmap())
        # p = painter.pen()
        # p.setWidth(4)
        # p.setColor(self.pen_color)
        # painter.setPen(p)
        # painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        # painter.end()
        # self.update()
        #
        # # Update the origin for next time.
        # self.last_x = e.x()
        # self.last_y = e.y()

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self.pen_color)
        painter.setPen(p)

        for n in range(SPRAY_PARTICLES):
            xo = random.randint(0, SPRAY_DIAMETER)
            yo = random.randint(0, SPRAY_DIAMETER)
            d = type(e.x())
            x = e.x() + xo
            y = e.y() + yo
            #point = QPoint(x, y)
            painter.drawPoint(x, y)



        self.update()

    # def mouseReleaseEvent(self, e):
    #     self.last_x = None
    #     self.last_y = None


COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]

class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)