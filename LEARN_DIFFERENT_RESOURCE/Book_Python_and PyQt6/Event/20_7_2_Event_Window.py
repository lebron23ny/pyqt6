from PyQt6 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def moveEvent(self, event):
        print('x = {0}; y = {1}'.format(event.pos().x(), event.pos().y()))
        QtWidgets.QWidget.moveEvent(self, event)

    def resizeEvent(self, event):
        print('w = {0}; h = {1}'.format(event.size().width(), event.size().height()))
        QtWidgets.QWidget.resizeEvent(self, event)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()