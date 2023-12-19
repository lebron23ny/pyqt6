from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QWidget, QVBoxLayout, QComboBox
import sys
from PyQt6.QtCore import Qt


class MyWind(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText('Line Edit 1')
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText('Line Edit 2')
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setPlaceholderText('Line Edit 3')

        self.lineEdit1.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lineEdit2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lineEdit3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)



        self.combobox1 = QComboBox()
        self.combobox1.addItems(['cmb1_1', 'cmb1_2'])

        self.combobox2 = QComboBox()
        self.combobox2.addItems(['cmb2_1', 'cmb2_2'])

        self.btn = QPushButton('Кнопка')
        self.btn.clicked.connect(self.btn_click)


        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.lineEdit3)
        layout.addWidget(self.combobox1)
        layout.addWidget(self.combobox2)
        layout.addWidget(self.btn)

        self.lineEdit3.setFocus()

        self.shortcut = QShortcut(QKeySequence('Ctrl+V'), self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.shortcut_method(shortcut_key))

    def shortcut_method(self, shortcut_key):
        if shortcut_key == 'Ctrl+V':
            print('Ctrl+V')
            print('lineEdit1 has focus : ', self.lineEdit1.hasFocus())
            print('lineEdit2 has focus : ', self.lineEdit2.hasFocus())
            print('lineEdit3 has focus : ', self.lineEdit3.hasFocus())
            print('combobox1 has focus : ', self.combobox1.hasFocus())
            print('combobox2 has focus : ', self.combobox2.hasFocus())
            print('btn has focus : ', self.btn.hasFocus())
            print()





    def btn_click(self):
        type_focus = self.btn.focusPolicy()
        name = type_focus.name
        value = type_focus.value
        print(f'name: {name}; value: {value}')
        flag = self.combobox1.hasFocus()
        print('lineEdit1 has focus : ', self.lineEdit1.hasFocus())
        print('lineEdit2 has focus : ', self.lineEdit2.hasFocus())
        print('lineEdit3 has focus : ', self.lineEdit3.hasFocus())
        print('combobox1 has focus : ', self.combobox1.hasFocus())
        print('combobox2 has focus : ', self.combobox2.hasFocus())
        print('btn has focus : ', self.btn.hasFocus())
        print()

app = QApplication(sys.argv)
win = MyWind()
win.show()
app.exec()