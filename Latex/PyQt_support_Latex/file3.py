import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QMainWindow, QApplication, QVBoxLayout, QWidget
from LatexFormulaWidget import LatexFormulaWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        widget = QWidget()
        self.setCentralWidget(widget)

        vlayout = QVBoxLayout()
        self.label1 = QLabel('123\nddd')
        self.label1.setStyleSheet('background-color: red')
        self.label2 = QLabel()
        self.pixmap = QPixmap()
        self.label3 = LatexFormulaWidget(r'$\sqrt{\alpha}\\\beta$')

        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.label3)


        widget.setLayout(vlayout)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()