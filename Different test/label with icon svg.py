from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon, QImage
import sys
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.label1 = QLabel('Label')
        self.button = QPushButton('Button')
        pixmap = QPixmap('icon.svg')
        icon = QIcon('icon.svg')
        self.label1.setPixmap(pixmap)
        self.label1.setScaledContents(True)

        self.label2 = QLabel('Label2')
        pixmap2 = QPixmap('ENERGOPROECT_LOGO.png')
        self.label2.setPixmap(pixmap2)
        self.label2.setScaledContents(True)


        self.button.setIcon(icon)

        self.label1.setStyleSheet('background-color: red')
        self.button.setStyleSheet('font-size: 22px; ')



        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.button)
        self.button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)


    def resizeEvent(self, a0):
        print(f'Размер формы: {self.size()}')
        print(f'размер лэйбла: {self.label1.size()}')






app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()

