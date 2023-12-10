#https://www.youtube.com/watch?v=p502guEpijk

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget, QFrame
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 420, 400
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
        QWidget {
        font-size: 30px;}
        ''')
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()


        self.frame = QFrame()
        self.frame.setStyleSheet("background-color: red;"
                                "border: 1px solid black;"
                                "border-radius:17px")
        self.frame.setLayout(self.layout1)
        self.layout.addWidget(self.frame)

        self.layout.addLayout(self.layout2, 7)

        #column1
        self.list = QListWidget()
        self.btn = QPushButton('Stop')
        self.layout1.addWidget(self.list)
        self.layout1.addWidget(self.btn)



        #column2
        self.btn2 = QPushButton('Start', clicked=self.resize_animation)
        self.layout2.addWidget(self.btn2)


    def resize_animation(self):
        self.animation = QPropertyAnimation(self.frame, b'geometry')
        self.animation.setDuration(500) #0.5 second
        if self.frame.width() == 276:
            self.animation.setStartValue(QRect(self.frame.x(), self.frame.y(), 276, self.frame.height()))
            self.animation.setEndValue(QRect(self.frame.x(), self.frame.y(), 100, self.frame.height()))
            self.animation.start()
        else:
            self.animation.setStartValue(QRect(self.frame.x(), self.frame.y(), 100, self.frame.height()))
            self.animation.setEndValue(QRect(self.frame.x(), self.frame.y(), 276, self.frame.height()))
            self.animation.start()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')