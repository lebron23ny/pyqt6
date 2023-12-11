from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QVBoxLayout, QApplication, QLineEdit, QTextEdit
from _My_Library.My_Widget.My_custom_title_bar import MyCustomTittleBar
from _My_Library.My_Widget.My_custom_title_bar1 import MyCustomTittleBar1
from PyQt6.QtCore import Qt
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        #self.setStyleSheet("QToolBar { border-left-style: none; border-right-style: none; }")

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowTitle("Title Bar")
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.layoutFrame = QVBoxLayout()
        self.layoutFrame.setSpacing(0)
        self.layoutFrame.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(frame)

        frame.setLayout(self.layoutFrame)
        self.title_bar = MyCustomTittleBar1(self)
        self.layoutFrame.addWidget(self.title_bar)


        self.layout_work_space = QVBoxLayout()
        self.layout_work_space.setContentsMargins(15, 5, 15, 5)
        self.layout_work_space.setSpacing(5)
        self.layoutFrame.addLayout(self.layout_work_space)

        self.label = QLabel('Label 1')
        self.label.setObjectName('Disc')
        self.button = QPushButton('Button 1')

        self.textEdit = QTextEdit()
        self.textEdit.setObjectName('Disc')

        self.layout_work_space.addWidget(self.label)
        self.layout_work_space.addWidget(self.textEdit)
        self.layout_work_space.addWidget(self.button)









app = QApplication(sys.argv)
app.setStyleSheet('''
    QLabel#Disc {
        border: 1px solid black;
        background-color:none;
        font-size: 30px;
        color: #93deed;
        border-radius: 1px;
        
    }
    QTextEdit#Disc {
    border: 1px solid black;
    font-size: 16pt;
    border-radius: 0px;
    background-color: transparent;
    
    }
    QFrame#TittleBarFrame {
        background-color: #FF4A7309;
        color: rgb(220, 220, 220);
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 20px;
    }
    QFrame {
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.369318 rgba(254, 93, 144, 255), stop:1 rgba(255, 255, 255, 255));
        background-color: #2F4454;
        
        color: rgb(220, 220, 220);
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 0px;
        border-top-left-radius: 0px;
        border-top-right-radius: 20px;
    }
    QPushButton
    {
        background-color: transparent;
        border: 1px solid black;
    }

    ''')

app.setStyle("Windows")
widget = MyWidget()
widget.show()
app.exec()