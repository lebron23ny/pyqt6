#https://www.youtube.com/watch?v=V482dnqiNqc&list=PL3JVwFmb_BnRpvOeIh_To4YSiebiggyXS&index=109
import sys
import time

from PyQt6.QtWidgets import QApplication, QProgressBar, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFrame
from PyQt6.QtCore import Qt, QTimer

class SplachScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Splash Screen Example')
        self.setFixedSize(1100, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) #атрибут указывает что Widget должен быть полупрозрачным

        self.counter = 0
        self.n = 300 #total instance

        self.initUI()


        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(200)


    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        self.labelTitle.resize(self.width()-10, 150)
        self.labelTitle.move(0, 40)
        self.labelTitle.setText('Splash Screen')
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Working on Task #1</strong>')
        self.labelDescription.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(0)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLoading.setText('laoding')

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.3):
            self.labelDescription.setText('<strong>Working on Task #2</strong>')
        elif self.counter == int(self.n * 0.6):
            self.labelDescription.setText('<strong>Working on Task #3</strong>')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            self.myApp = MyApp()
            self.myApp.show()

        self.counter += 1












class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    #LabelTitle {
        font-size: 60px;
        color: #93deed;
    }
    #LabelDesc {
        font-size: 30px;
        color: #c2ced1;
    }
    #LabelLoading {
        font-size: 30px;
        color: #e8e8eb
    }
    QFrame {
        background-color: #2F4454;
        color: rgb(220, 220, 220);
        border-radius: 20px;
    }
    QProgressBar {
        background-color: #DA7B93;
        color: rgd(200, 200, 200);
        border-style: none;
        border-radius: 10px;
        text-align: center;
        font-size: 30px;
    }
    QProgressBar::chunk {
        border-radius: 10px;
        background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
        
        }
    
    
    ''')

    # myApp = MyApp()
    # myApp.show()
    splash = SplachScreen()
    splash.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')


