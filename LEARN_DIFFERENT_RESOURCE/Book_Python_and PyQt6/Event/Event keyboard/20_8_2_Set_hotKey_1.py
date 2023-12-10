from PyQt6 import QtWidgets, QtCore, QtGui


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = None
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.shortcut_Alt_C = QtGui.QShortcut(QtGui.QKeySequence('Alt+C'), self)
        self.shortcut_Alt_C.setContext(QtCore.Qt.ShortcutContext.WidgetShortcut)

        self.shortcut_Alt_V = QtGui.QShortcut(QtGui.QKeySequence('Alt+V'), self)


    def event(self, event):
        if event.type() == QtCore.QEvent.Type.Shortcut:
            if self.id == event.shortcutId():
                self.setFocus(QtCore.Qt.FocusReason.ShortcutFocusReason)
                return True
        return QtWidgets.QLineEdit.event(self, event)




class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_Widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_Widget)
        self.resize(300, 100)

        self.label = QtWidgets.QLabel('Установи фокус на поле 1', self.central_Widget)

        self.lineEdit1 = QtWidgets.QLineEdit(self.central_Widget)
        self.label.setBuddy(self.lineEdit1)


        self.lineEdit2 = MyLineEdit(self.central_Widget)
        self.lineEdit1.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)

        self.lineEdit2.shortcut_Alt_C.activated.connect(self.shortCut_Alt_C)
        self.lineEdit2.shortcut_Alt_V.activated.connect(self.shortCut_Alt_V)

        self.button = QtWidgets.QPushButton('Убрать фокус с поля 1', self.central_Widget)
        self.vbox = QtWidgets.QVBoxLayout(self.central_Widget)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.button)
        self.clipboard = QtWidgets.QApplication.clipboard()
        #self.setLayout(self.vbox)

        self.button.clicked.connect(self.on_clicked)

    def keyPressEvent(self, event):
        k = event.key()



        k1 = QtCore.Qt.Key.Key_C
        modifiers = event.modifiers()
        type1 = type(event)
        name = modifiers.name
        text = event.text()
        standardKey = QtGui.QKeySequence.StandardKey.Copy
        d = event.matches(standardKey)


        if event.modifiers() == QtCore.Qt.Modifier.MODIFIER_MASK:
            print('удерживается Ctrl')

        if event.key() == QtCore.Qt.Key.Key_Shift:
            print('shift press')

        if event.key() == QtCore.Qt.Key.Key_Shift:
            print('ctrl')

        if event.key() == QtCore.Qt.Key.Key_C and event.modifiers().name == 'ControlModifier':
            print('ctrl+C')

        if event.key() == QtCore.Qt.Key.Key_D and event.modifiers().name == 'ControlModifier':

            print('ctrl+D')

        super(MyWindow, self).keyPressEvent(event)


    def on_clicked(self):
        self.lineEdit1.clearFocus()


    def shortCut_Alt_C(self):
        if self.lineEdit2.hasFocus():
            print('Alt+C')

    def shortCut_Alt_V(self):
        if self.lineEdit2.hasFocus():
            print('Alt+V')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()