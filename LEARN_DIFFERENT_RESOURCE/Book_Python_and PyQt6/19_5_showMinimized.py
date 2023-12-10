import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('label1')
        self.label2 = QLabel('label2')
        self.label3 = QLabel('label3')
        self.buttonMin = QPushButton('Свернуть')
        self.buttonMax = QPushButton('Развернуть')
        self.buttonFull = QPushButton('Полный экран')
        self.buttonNormal = QPushButton('Нормальный размер')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)


        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.buttonMin)
        self.layout.addWidget(self.buttonMax)
        self.layout.addWidget(self.buttonFull)
        self.layout.addWidget(self.buttonNormal)


        self.buttonMin.clicked.connect(self.btnMin_click)
        self.buttonMax.clicked.connect(self.btnMax_click)
        self.buttonFull.clicked.connect(self.btnFull_click)
        self.buttonNormal.clicked.connect(self.btnNormal_click)

    def btnMin_click(self):
        self.showMaximized()


    def btnMax_click(self):
        self.showMaximized()

    def btnFull_click(self):
        self.showFullScreen()

    def btnNormal_click(self):
        self.showNormal()



app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()