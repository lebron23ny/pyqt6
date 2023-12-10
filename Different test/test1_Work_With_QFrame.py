from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QFrame, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 10, 10, 10)

        Widget = QWidget()

        self.label = QLabel('Label')
        self.label.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button = QPushButton("Button")
        self.button.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')
        vBox = QVBoxLayout()
        vFrame = QFrame()
        vbox_for_Frame = QVBoxLayout()
        vbox_for_Frame.addWidget(vFrame)


        vFrame.setStyleSheet(u"background-color: red;\n"
"border: 1px solid black;\n"
"border-radius:17px")
        vBox.setContentsMargins(0, 0, 0, 0)
        vBox.setSpacing(2)
        vBox.addWidget(self.label)
        vBox.addWidget(self.button)
        vBox.addLayout(vbox_for_Frame)
        vbox_in_Frame = QVBoxLayout(vFrame)
        vbox_in_Frame.setSpacing(10)
        vbox_in_Frame.setContentsMargins(10, 10, 10, 10)

        self.labelFrame = QLabel()
        self.labelFrame.setText('Label Frame')
        self.labelFrame.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')
        self.buttonFrame = QPushButton()
        self.buttonFrame.setText('Button Frame')
        self.buttonFrame.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')

        vbox_in_Frame.addWidget(self.labelFrame)
        vbox_in_Frame.addWidget(self.buttonFrame)


        frame2 = QFrame()
        frame2.setStyleSheet(u"background-color: blue;\n"
"border: 1px solid black;\n"
"border-radius:17px")
        vbox_in_Frame2 = QVBoxLayout()
        frame2.setLayout(vbox_in_Frame2)
        self.lable3 = QLabel('Label 3')
        self.lable3.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')
        self.button3 = QPushButton('Button 3')
        self.button3.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')
        vbox_in_Frame2.addWidget(self.lable3)
        vbox_in_Frame2.addWidget(self.button3)

        vBox.addWidget(frame2)




        Widget.setLayout(vBox)
        self.setCentralWidget(Widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
