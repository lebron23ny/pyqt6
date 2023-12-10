import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow,  QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setMouseTracking(False)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        if e.button() == Qt.MouseButton.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.label.setText("mouseMoveEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.label.setText("mouseMoveEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.label.setText("mouseMoveEvent RIGHT")


    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
       # super(self, MainWindow).contextMenuEvent(e)

        if e.button() == Qt.MouseButton.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.label.setText("mousePressEvent LEFT")



        elif e.button() == Qt.MouseButton.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
