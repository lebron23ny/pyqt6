
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

class BreakLineV(QFrame):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setFixedWidth(25)
        self.setStyleSheet('background-color:gray')





class BreakLineH(QFrame):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setFixedHeight(5)
        self.setStyleSheet('background-color:gray')
        self.initial_pos = None


    def mousePressEvent(self, event):
        self.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):

        #self.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.setCursor(QCursor(Qt.CursorShape.SplitVCursor))

        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            delta_x = delta.x()
            delta_y = delta.y()

            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y()
                                )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.CursorShape.SplitVCursor))
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()
