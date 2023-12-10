from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import pyqtSignal

class CustomButton(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text=None, pixmap=None):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.startColor = self.palette().color(QPalette.ColorRole.Window)
        self.setMouseTracking(True)
        self.setObjectName('CustomButton')

        if pixmap is not None:
            size = pixmap.size()
            height = size.height() + 50
            width = size.width() + 20
            self.setPixmap(pixmap)
            self.setFixedSize(height, width)

    def mouseMoveEvent(self, ev):
        self.setStyleSheet('background-color: blue;'
                           'border: 10px solid black;'
                           'font-weight:bold;')

    def mousePressEvent(self, ev):
        self.setStyleSheet('color: black;'
                           'background-color: gold;'
                           'border: 10px solid black;'
                           'font-weight:bold;')
        self.clicked.emit()

    def mouseReleaseEvent(self, ev):
        self.setStyleSheet(f'background-color: {self.startColor}')

    def leaveEvent(self, a0):
        self.setStyleSheet(f'background-color: {self.startColor}')