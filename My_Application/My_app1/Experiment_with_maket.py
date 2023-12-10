import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, \
    QLineEdit, QSizePolicy, QTabWidget, QMainWindow
from PyQt6 import QtGui, QtCore


class MyButton(QWidget):
    def __init__(self, text):
        super().__init__()

        layout = QVBoxLayout()
        self.button = QPushButton(text)
        self.button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        layout.addWidget(self.button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)


class MyLineEdit(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.lineEdit = QLineEdit()
        self.lineEdit.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        layout.addWidget(self.lineEdit)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)







class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QVBoxLayout')

        # create a layout

        tabWidget = QTabWidget()
        tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        tabWidget.setMovable(True)
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()

        tabWidget.addTab(self.tab_1, 'Вкладка 1')
        tabWidget.addTab(self.tab_2, 'Вкладка 2')

        tabWidget.setCurrentIndex(0)

        self.setCentralWidget(tabWidget)

        layout_main_tab1 = QVBoxLayout()





        label_Title = QLabel('Label Title')
        label_Title.setStyleSheet('background-color: red')
        label_Title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        #label_Title.setMinimumSize(10, 100)
        label_Title.setFixedHeight(100)


        label1 = QLabel("Label 1")
        label1.setStyleSheet('background-color: lightgreen')


        lineEdit1 = QLineEdit()
        lineEdit1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        #lineEdit1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        bt1 = QPushButton('Buttnon 1')
        bt1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        bt1.setStyleSheet('background-color: purple')




        label2 = QLabel("Label 2")
        label2.setStyleSheet('background-color: blue')

        lineEdit2 = QLineEdit()
        lineEdit2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)



        bt2 = QPushButton('Buttnon 2')
        bt2.setStyleSheet('background-color: lime')
        bt2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        label3 = QLabel("Label 3")
        label3.setStyleSheet('background-color: Olive')
        label3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        lineEdit3 = QLineEdit()
        lineEdit3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        bt3 = QPushButton('Buttnon 3')
        bt3.setStyleSheet('background-color: Cyan')
        bt3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        label4 = QLabel("Label 4")
        bt4 = MyButton('My Button 4')
        bt4.setStyleSheet('background-color: Cyan')
        lineEdit4 = MyLineEdit()



        label_finish =QLabel('Label End')
        label_finish.setStyleSheet('background-color: Gold')

        label_finish.setFixedHeight(100)


        layout_main_tab1 = QVBoxLayout()
        layout_v1 = QHBoxLayout()



        layout_v2 = QHBoxLayout()
        layout_v3 = QHBoxLayout()
        layout_v4 = QHBoxLayout()

        #Добавления виджетов в сетки
        layout_v1.addWidget(label1)
        layout_v1.addWidget(lineEdit1)
        layout_v1.addWidget(bt1)

        layout_v2.addWidget(label2)
        layout_v2.addWidget(lineEdit2)
        layout_v2.addWidget(bt2)

        layout_v3.addWidget(label3)
        layout_v3.addWidget(lineEdit3)
        layout_v3.addWidget(bt3)

        layout_v4.addWidget(label4)
        layout_v4.addWidget(lineEdit4)
        layout_v4.addWidget(bt4)


        #Установка фактора растягивания (чтобы задавать ширину пропроционально друг другу
        #Ширина лейбла и лайн едит будет в два раза меньше чем ширина кнопки 6/3 = 2
        #Нужно задавать целые числоа


        layout_v1.setStretchFactor(label1, 3)
        layout_v1.setStretchFactor(lineEdit1, 3)
        layout_v1.setStretchFactor(bt1, 6)


        layout_v2.setStretchFactor(label2, 3)
        layout_v2.setStretchFactor(lineEdit2, 3)
        layout_v2.setStretchFactor(bt2, 6)


        layout_v3.setStretchFactor(label3, 3)
        layout_v3.setStretchFactor(lineEdit3, 3)
        layout_v3.setStretchFactor(bt3, 6)


        layout_v4.setStretchFactor(label4, 3)
        layout_v4.setStretchFactor(lineEdit4, 3)
        layout_v4.setStretchFactor(bt4, 6)

        #Добавление виджетов и слоев в главный слой

        layout_main_tab1.addWidget(label_Title)
        layout_main_tab1.addLayout(layout_v1)
        layout_main_tab1.addLayout(layout_v2)
        layout_main_tab1.addLayout(layout_v3)

        layout_main_tab1.addLayout(layout_v4)

        layout_main_tab1.addWidget(label_finish)


        layout_v1.setSpacing(0)
        layout_v1.setContentsMargins(0, 0, 0, 0)

        layout_main_tab1.setContentsMargins(0, 0, 0, 0)
        layout_main_tab1.setSpacing(0)
        self.tab_1.setLayout(layout_main_tab1)














if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())