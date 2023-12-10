import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QLineEdit, QTableWidget

#КОГДА ФОКУС ПОМЕЩЕН В ЭЛЕМЕНТ В КОТОРЫЙ МОЖНО ВСТАВИТЬ ДАННЫЕ (QLINEEDIT ИЛИИ QTABLEWIDGET) ГОРЯЧИЕ КЛАВИЩИ НЕ РАБОТАЮТ

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.label = QLabel('Установи фокус на поле 1')
        self.lineEdit1 = QLineEdit()
        self.tableWidget = QTableWidget(3, 3)



        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.tableWidget)

        #Basic shortcut
        self.shortcut = QShortcut(QKeySequence('Alt+C'), self)
        self.shortcut.activated.connect(lambda shortcut_key=self.shortcut.key().toString(): self.displayKeys(shortcut_key))

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

        self.lineEdit1.clearFocus()





    def displayKeys(self, mapping):
        print(mapping)



app = QApplication(sys.argv)
window = AppDemo()
window.show()
app.exec()