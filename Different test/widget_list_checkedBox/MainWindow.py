from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import Qt
import sys
from Widget import CheckList




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Лист чекбокс')
        self.widget = QWidget()
        layot = QVBoxLayout()
        self.widget.setLayout(layot)



        self.checkedList = CheckList(['B15', 'B20', 'B25'])
        self.button = QPushButton('Нажми')
        self.button.clicked.connect(self.the_heandler)
        layot.addWidget(self.checkedList)
        layot.addWidget(self.button)


        self.setCentralWidget(self.widget)


    def the_heandler(self):
        for index in range(self.checkedList.count()):
            if self.checkedList.item(index).checkState() == Qt.CheckState.Checked:

                print(self.checkedList.item(index).text())

        print()






app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()


