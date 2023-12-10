#https://www.youtube.com/watch?v=ORJI3_DbJyE&list=PL3JVwFmb_BnRpvOeIh_To4YSiebiggyXS&index=5

import sys
from PyQt6.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt6.QtCore import QBasicTimer
from PyQt6.QtCore import Qt


class PregressBarDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.progressBar = QProgressBar(self, objectName="BlueProgressBar")
        self.progressBar.setStyleSheet('#BlueProgressBar {border: 2px solid #2196F3; '
                                       'border-radius: 5px; '
                                       'background-color: #E0E0E0;}'
                                       '#BlueProgressBar::chunk {'
                                       'background-color: #2196F3;'
                                       'width: 10px; '
                                       'margin: 0.5px;}'
                                       )
        self.progressBar.setGeometry(30, 40, 200, 25)

        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(30, 80)
        self.btnStart.clicked.connect(self.startProgress)

        self.btnReset = QPushButton('Reset', self)
        self.btnReset.move(120, 80)
        self.btnReset.clicked.connect(self.resetBar)


        self.timer = QBasicTimer()
        self.step = 0

    def startProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnStart.setText('Start')
        else:
            self.timer.start(100, self)
            self.btnStart.setText('Stop')

    def resetBar(self):
        self.step = 0
        self.progressBar.setValue(self.step)


    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btnStart.setText('Start')
            return
        self.step += 1
        self.progressBar.setValue(self.step)

StyleSheet = '''
        

        #BlueProgressBar {
            border: 2px solid #2196F3;     
            border-radius: 5px;
            background-color: #E0E0E0;
        }
        #BlueProgressBar::chunk {
            background-color: #2196F3;
            width: 10px;                   
            margin: 0.5px;
        }
        '''

if __name__ =='__main__':
    app = QApplication(sys.argv)
    #app.setStyleSheet(StyleSheet)
    demo = PregressBarDemo()
    demo.show()



    sys.exit(app.exec())