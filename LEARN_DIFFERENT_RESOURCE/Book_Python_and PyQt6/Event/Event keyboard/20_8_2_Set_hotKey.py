from PyQt6 import QtWidgets, QtCore, QtGui


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = None


    def event(self, event):
        if event.type() == QtCore.QEvent.Type.Shortcut:
            if self.id == event.shortcutId():
                self.setFocus(QtCore.Qt.FocusReason.ShortcutFocusReason)
                return True
        return QtWidgets.QLineEdit.event(self, event)




class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

        self.label = QtWidgets.QLabel('Установи фокус на поле 1')

        self.lineEdit1 = QtWidgets.QLineEdit()
        self.label.setBuddy(self.lineEdit1)


        self.lineEdit2 = MyLineEdit()

        self.lineEdit2.id = self.lineEdit2.grabShortcut(QtGui.QKeySequence.mnemonic('&e'))
        # self.lineEdit2.id = self.lineEdit2.grabShortcut(QtGui.QKeySequence('Alt+C'))
        # self.lineEdit2.id = self.lineEdit2.grabShortcut(QtGui.QKeySequence('Alt+D'))

        self.button = QtWidgets.QPushButton('Убрать фокус с поля 1')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.button.clicked.connect(self.on_clicked)


    def on_clicked(self):
        self.lineEdit1.clearFocus()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()