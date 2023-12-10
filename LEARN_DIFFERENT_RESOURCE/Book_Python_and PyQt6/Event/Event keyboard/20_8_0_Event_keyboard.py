from PyQt6.QtWidgets import QPushButton, QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        self.text = QLineEdit('text 1')
        self.text2 = QLineEdit('text 2')
        self.button = QPushButton('Button')

        self.layout = QVBoxLayout()

        widget.setLayout(self.layout)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.btn_click)

    def btn_click(self):
        self.text2.setFocus(Qt.FocusReason.MouseFocusReason)
        self.text.clearFocus()
        widget = self.focusWidget()
        tex = widget.text()
        print('LineEdit2 has focus: ', self.text2.hasFocus())
        print('LineEdit1 has focus: ', self.text.hasFocus())


app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()
