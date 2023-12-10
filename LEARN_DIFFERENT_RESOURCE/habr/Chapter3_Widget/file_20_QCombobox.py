import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        layout = QVBoxLayout()
        self.nane_Title = "My App"

        self.setWindowTitle(self.nane_Title)

        self.widget = QComboBox()
        self.widget.addItems(["One", "Two", "Three"])

        button = QPushButton('Вставить четвертый элемент')

        layout.addWidget(self.widget)

        layout.addWidget(button)

        widget1 = QWidget()
        widget1.setLayout(layout)




        # Отправляет текущий индекс (позицию) выбранного элемента.
        self.widget.currentIndexChanged.connect( self.index_changed )

        # Есть альтернативный сигнал отправки текста.
        self.widget.currentTextChanged.connect( self.text_changed )


        button.clicked.connect(self.my_button_click)

        self.setCentralWidget(widget1)


    def my_button_click(self):
        print('Кнопка')
        self.widget.addItems(['four', 'five'])


    def index_changed(self, i): # i — это int
        if self.nane_Title == 'My App':
            self.nane_Title = str(i)
            self.setWindowTitle(self.nane_Title)
        else:
            temp_text = self.windowTitle()
            temp_text += f' {i}'
            self.nane_Title = temp_text
            self.setWindowTitle(temp_text)

        print(i)

    def text_changed(self, s): # s — это str
        if self.nane_Title == 'My App':
            self.nane_Title = s
            self.setWindowTitle(self.nane_Title)
        else:
            temp_text = self.windowTitle()
            temp_text += f' {s}'
            self.nane_Title = temp_text
            self.setWindowTitle(temp_text)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()