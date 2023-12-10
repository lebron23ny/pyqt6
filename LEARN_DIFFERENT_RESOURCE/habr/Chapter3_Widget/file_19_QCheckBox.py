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

        self.setWindowTitle("My App")

        self.widget = QCheckBox()
        self.widget.setTristate(True)
        self.widget.setCheckState(Qt.CheckState.PartiallyChecked)

        self.widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(self.widget)

    def show_state(self, s):
        s == Qt.CheckState.Checked
        if s == 0:
            self.setWindowTitle("Не отмечен")
        elif s == 1:
            self.setWindowTitle('Отмечен частично')
        else:
            self.setWindowTitle('Отмечен')
        print(s == Qt.CheckState.Checked)
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()