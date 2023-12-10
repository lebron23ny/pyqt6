import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon
from my_app1 import App1_MainWindow
from my_app2_version3_2 import App2_Mainwindow

from _My_Library.My_Widget.My_custom_button import CustomButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        hLayout = QHBoxLayout()
        vLayot = QVBoxLayout()
        widget.setLayout(hLayout)

        self.button_show_app1 = QPushButton('Приложение 1')
        self.button_show_app1.setIcon(QIcon('ENERGOPROECT_LOGO.png'))
        self.button_show_app1.setIconSize(QSize(33, 33))

        self.button_show_app2 = CustomButton('Приложение 2')
        self.button_show_app3 = QPushButton('Приложение 3')
        self.button_show_app3.setIcon(QIcon('ENERGOPROECT_LOGO.png'))
        self.button_show_app3.setIconSize(QSize(33, 33))
        self.button_show_app4 = QPushButton('Приложение 4')
        self.label = CustomButton("Custom Widget")
        pixmap = QPixmap('ENERGOPROECT_LOGO.png')
        self.pixmap = pixmap.scaled(112, 112, Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        self.custom_button = CustomButton(pixmap=self.pixmap)

        self.app1 = App1_MainWindow()
        self.app2 = App2_Mainwindow()
        self.app1.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.app2.setWindowModality(Qt.WindowModality.ApplicationModal)

        hLayout.addWidget(self.button_show_app1, 10)
        hLayout.addWidget(self.button_show_app2, 25)

        vLayot.addWidget(self.button_show_app3, 4)
        vLayot.addWidget(self.button_show_app4, 6)
        vLayot.addWidget(self.label, 10)
        vLayot.addWidget(self.custom_button, 10)
        hLayout.addLayout(vLayot, 3)
        self.set_style_default()
        self.BindingSignal()

    def set_style_default(self):
        self.setMinimumWidth(800)
        self.setMinimumHeight(425)

        self.button_show_app1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button_show_app2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button_show_app3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button_show_app4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        pixmap_app1 = QPixmap('ENERGOPROECT_LOGO.png')
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

    def BindingSignal(self):
        self.button_show_app1.clicked.connect(self.click_btn1)
        self.button_show_app2.clicked.connect(self.click_btn2)
        self.custom_button.clicked.connect(self.click_custon_buttom)

    def click_btn1(self):
        self.app1.show()

    def click_btn2(self):
        self.app2.show()

    def click_custon_buttom(self):
        print('Нажат пользовательский виджет')
        size = self.pixmap.size()
        width = size.width() + 20
        height = size.height() + 20
        size1 = QSize(height, width)
        print(self.pixmap.size())


StyleSheet = """

QMainWindow {
    background-color: #FF00B379;
}
QLabel#name_property
{
     color: black;
     background-color:red;
     font-size:15pt;
     font: bold;
     border: none;
     padding-left:10px;
     padding-right:100px;
     padding-top:1px
}

QLabel#label_formula
{
    background-color:red;
    font: bold;
    border: none;
    padding-left:10px;
    padding-right:100px;
    padding-top:1px;
}

QLabel {
    color: blue;
    background-color: black;
    border: 2px solid black;
    
    font-size:15pt;
    font-family:GOST 2.304 type A;
}
QLabel#CustomButton {
    color: white;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
}

QLabel#label_standard {
    color: black;
    font-size:15pt;
    font-family:GOST 2.304 type A;
    border: 2px solid black;
    border-radius: 10px;
    background-color: red;
    padding-left:20px;     
}

QPushButton {
    color: white;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
}
QPushButton:hover {
    color: black;
    background-color: gold;
    font-weight:bold;


}
QPushButton:pressed {
    color: gold;
    background-color: red;

}
QComboBox {
    background-color: red;
    border: 2px solid black;
    border-radius: 10px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
    font-size:15pt;
    font-family:GOST 2.304 type A;
}
QComboBox QAbstractItemView {
    border: 2px solid blue;
    selection-background-color: red;
    background-color: yellow;
    border-radius: 10px;
}

"""

app = QApplication(sys.argv)
app.setStyleSheet(StyleSheet)
window = MainWindow()
window.show()
app.exec()
