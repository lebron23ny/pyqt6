#https://habr.com/ru/companies/skillfactory/articles/599599/


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def  the_button_was_clicked(self):
        print('Clicked')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()