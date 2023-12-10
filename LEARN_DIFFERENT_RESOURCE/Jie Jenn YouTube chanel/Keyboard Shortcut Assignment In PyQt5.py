#https://www.youtube.com/watch?v=xnTPZ5fHvCc&list=PL3JVwFmb_BnRpvOeIh_To4YSiebiggyXS&index=68

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtWidgets import QWidget, QLabel, QApplication


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        self.display = QLabel()
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setGeometry(1500, 1000, 600, 200)
        self.display.setStyleSheet('font-size: 60px')

        #Basic shortcut
        self.shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
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





    def displayKeys(self, mapping):
        self.display.setText(mapping)
        self.display.show()



app = QApplication(sys.argv)
window = AppDemo()
window.show()
app.exec()