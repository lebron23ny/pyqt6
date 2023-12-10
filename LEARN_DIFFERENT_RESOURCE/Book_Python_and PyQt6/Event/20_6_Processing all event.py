from PyQt6 import QtCore, QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def event(self, event):
        if event.type() == QtCore.QEvent.Type.KeyPress:
            print('Нажата клавиша на клавиатуре')
            print('Код: ', event.key(), ', текст: ', event.text())
        elif event.type() == QtCore.QEvent.Type.Close:
            print('Окно закрыто')
        elif event.type() == QtCore.QEvent.Type.MouseButtonPress:
            p = event.pos()
            print('Щелчок мышью. Координаты: ', p.x(), p.y())
        return QtWidgets.QWidget.event(self, event)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()





