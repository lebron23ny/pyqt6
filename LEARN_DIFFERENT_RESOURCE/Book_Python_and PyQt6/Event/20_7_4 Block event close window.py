
from PyQt6 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def closeEvent(self, event):
        result =QtWidgets.QMessageBox.question(self, 'Подтверждае закрытия окна',
                                               'Вы действительно хотите закрыть окно?')

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            event.acceptt()
            QtWidgets.QWidget.closeEvent(self, event)
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()