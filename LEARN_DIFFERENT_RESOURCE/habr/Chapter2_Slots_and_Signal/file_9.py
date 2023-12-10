#https://habr.com/ru/companies/skillfactory/articles/599599/


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Также меняем заголовок окна.
        self.setWindowTitle("My Oneshot App")


    def the_button_was_pressed(self):
        text = self.button.text()
        print(f'Кнопка, {text}, подожди не отпускай меня')


    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print('О нет, зачем ты отпустил меня?')
        print(self.button_is_checked)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()