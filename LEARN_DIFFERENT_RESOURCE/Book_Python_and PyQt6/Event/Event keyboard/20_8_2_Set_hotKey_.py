from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QKeySequence, QShortcut


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = None

        # self.shortcut_Alt_C = QtGui.QShortcut(QtGui.QKeySequence('Alt+C'), self)
        # #self.shortcut_Alt_C.setContext(QtCore.Qt.ShortcutContext.WidgetShortcut)
        # self.shortcut_Alt_V = QtGui.QShortcut(QtGui.QKeySequence('Alt+V'), self)
        # self.shortcut_Ctrl_C = QtGui.QShortcut(QtGui.QKeySequence.StandardKey.Copy, self)
        # self.shortcut_Ctrl_V = QtGui.QShortcut(QtGui.QKeySequence.StandardKey.Paste, self)

        # self.shortcut = QtGui.QShortcut(QtGui.QKeySequence('Alt+C'), self)
        # #self.shortcut_Alt_C.setContext(QtCore.Qt.ShortcutContext.WidgetShortcut)
        # self.shortcut = QtGui.QShortcut(QtGui.QKeySequence('Alt+V'), self)
        # self.shortcut = QtGui.QShortcut(QtGui.QKeySequence.StandardKey.Copy, self)
        # self.shortcut = QtGui.QShortcut(QtGui.QKeySequence.StandardKey.Paste, self)







class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

        self.label = QtWidgets.QLabel('Установи фокус на поле 1')

        self.lineEdit1 = QtWidgets.QLineEdit()
        #self.label.setBuddy(self.lineEdit1)


        self.lineEdit2 = MyLineEdit()




        self.button = QtWidgets.QPushButton('Убрать фокус с поля 1')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.button.clicked.connect(self.on_clicked)

        # Basic shortcut
        self.shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.displayKeys(shortcut_key))

        # Standard shortcut
        self.shortcut = QShortcut(QKeySequence.StandardKey.Paste, self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.displayKeys(shortcut_key))

        self.shortcut = QShortcut(QKeySequence.StandardKey.Copy, self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.displayKeys(shortcut_key))

        # Special Keys assigment
        self.shortcut = QShortcut(QKeySequence('Ctrl+Shift+T'), self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.displayKeys(shortcut_key))

        # key sequence order
        self.shortcut = QShortcut(QKeySequence('Ctrl+Shift+Space'), self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.displayKeys(shortcut_key))


    def displayKeys(self, mapping):
        t = self.lineEdit2.shortcut.key().toString()
        print(mapping)

    def on_clicked(self):
        self.lineEdit1.clearFocus()


    def shortCut_Alt_C(self):

        print('Alt+C')

    def shortCut_Alt_V(self):

        print('Alt+V')


if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()