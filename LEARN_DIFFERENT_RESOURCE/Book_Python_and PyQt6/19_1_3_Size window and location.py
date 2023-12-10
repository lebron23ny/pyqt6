from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame,
                             QSizePolicy)
from PyQt6.QtCore import Qt, QSize, QRect, QRectF
import sys

from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitializeComponent()
        self.BindingSignal()
        self.SetStyles()



    def InitializeComponent(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName('central_widget')
        self.layout_central_widget = QVBoxLayout()






        self.break_line3 = QFrame()
        self.break_line3.setFrameShape(QFrame.Shape.HLine)
        self.break_line3.setFrameShadow(QFrame.Shadow.Sunken)


        self.break_line4 = QFrame()
        self.break_line4.setFrameShape(QFrame.Shape.VLine)
        self.break_line4.setFrameShadow(QFrame.Shadow.Sunken)
        self.break_line4.setStyleSheet('background-color:black;')



        self.layout = QHBoxLayout()
        self.label11 = QLabel('Label 11')
        self.label22 = QLabel('Label 22')
        self.label33 = QLabel('Label 33')
        self.layout.addWidget(self.label11)

        self.layout.addWidget(self.label22)

        self.layout.addWidget(self.label33)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout_central_widget)
        self.label1 = QLabel('Label 1')
        self.label2 = QLabel('Label 2')
        self.label3 = QLabel('Label 3')
        self.label3.setObjectName('variant2')
        self.label4 = QLabel('Label 4')
        self.label4.setObjectName('variant1')
        self.label5 = QLabel('Label 5')

        self.label5.setObjectName('variant1')
        self.button = QPushButton('Delete Widget')
        self.button2 = QPushButton('Movable')
        self.button3 = QPushButton('Увеличить окно в два раза')
        self.button4 = QPushButton('Подвинуть окно')
        self.button_aligment = QPushButton('Выровнить окно по центру экрана')

        self.layout_central_widget.addWidget(self.label1)
        self.layout_central_widget.addWidget(self.label2)
        self.layout_central_widget.addWidget(self.label3)
        self.layout_central_widget.addWidget(self.label4)
        self.layout_central_widget.addWidget(self.label5)

        self.layout_central_widget.addWidget(self.button)
        self.layout_central_widget.addWidget(self.button2)
        self.layout_central_widget.addWidget(self.button3)
        self.layout_central_widget.addWidget(self.button4)
        self.layout_central_widget.addWidget(self.button_aligment)

        self.layout_central_widget.setStretch(0, 1)
        self.layout_central_widget.setStretch(1, 1)
        self.layout_central_widget.setStretch(2, 1)
        self.layout_central_widget.setStretch(3, 2)
        self.layout_central_widget.setStretch(4, 2)
        self.layout_central_widget.setStretch(5, 8)
        self.layout_central_widget.setStretch(6, 4)
        self.layout_central_widget.setStretch(7, 2)




    def SetStyles(self):
        self.setStyleSheet('background-color:#FF5241BE')
        self.setMinimumHeight(400)
        self.button3.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.button3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)


    def BindingSignal(self):
        self.button.clicked.connect(self.click_btn)
        self.button2.clicked.connect(self.click_btn2)
        self.button3.clicked.connect(self.click_btn3)
        self.button4.clicked.connect(self.click_btn4_move)
        self.button_aligment.clicked.connect(self.click_aligment)




    def click_aligment(self):
        screen_size = self.screen().size()
        width_screen = screen_size.width()
        height_screen = screen_size.height()

        width_window = self.width()
        height_window = self.height()

        x = int((width_screen - width_window)/2)
        y = int((height_screen - height_window)/2)

        self.move(x, y)


    def click_btn4_move(self):
        geometry = self.frameGeometry()
        pad_x = geometry.x() + 10
        pad_y = geometry.y()
        size_screen = self.screen().size()
        move = self.move(pad_x, pad_y)

    def click_btn2(self):
        index = self.layout_central_widget.indexOf(self.button2)
        widget_top = self.layout_central_widget.itemAt(index - 1).widget()
        widget_bottom = self.layout_central_widget.itemAt(index - 2).widget()

        height_window = self.height()
        width_window = self.width()
        size_window = self.size()

        pad_top_window = self.x()
        pad_left_window = self.y()

        height_top_widget = widget_top.height()
        height_bottom_widget = widget_bottom.height()

        width_top_widget = widget_top.width()
        width_bottom_widget = widget_bottom.width()

        # widget_bottom.setMinimumHeight(height_bottom_widget + 10)
        # widget_top.setMinimumHeight(height_top_widget - 10)

        widget_bottom.setFixedHeight(height_bottom_widget + 10)
        widget_top.setFixedHeight(height_top_widget - 10)

        # widget_bottom.resize(width_bottom_widget, height_bottom_widget + 10)
        # widget_top.resize(width_top_widget, height_top_widget - 10)

        self.resize(QSize(width_window, height_window))




    def click_btn(self):

        index_delete = 0
        item_element = self.layout_central_widget.itemAt(index_delete)
        item_element_widget = item_element.widget()
        item_element_layout = item_element.layout()
        if type(item_element_widget) is not QPushButton:
            self.layout_central_widget.takeAt(index_delete)
            if item_element_widget is not None:
                item_element_widget.deleteLater()
            if item_element_layout is not None:
                while item_element_layout.count() > 0:
                    widget_in_layout = item_element_layout.takeAt(0).widget()
                    widget_in_layout.deleteLater()
                item_element_layout.deleteLater()


    def click_btn3(self):

        stretch_list = []
        height_widget_list = []
        for i in range(self.layout_central_widget.count()):
            stretch_list.append(self.layout_central_widget.stretch(i))
            h = self.layout_central_widget.itemAt(i).widget().height()
            height_widget_list.append(h)

        print(stretch_list)
        print()
        print(height_widget_list)


        height_window = self.height()
        width_window = self.width()
        self.resize(2 * width_window, 2*height_window)
        factor = self.layout_central_widget.stretch(3)
        print(factor)










StyleSheet = """

QMainWindow {
    background-color: green;
}
QLabel {
    color: white;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
    padding-left:15px;

}
QLabel#variant1 {
    color: red;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
    padding-left:15px;
}
QLabel#variant2 {
    color: blue;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
    padding-left:15px;
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

"""

app = QApplication(sys.argv)
app.setStyleSheet(StyleSheet)
window = MainWindow()
window.show()
app.exec()