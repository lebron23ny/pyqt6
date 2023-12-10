import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QLabel, QLineEdit, QVBoxLayout,
                             QGridLayout, QHBoxLayout, QSizePolicy)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



from My_Library.Calculate import findZ, isNumberValue
from My_Library.Calculate import listX, listY, listZ

from My_Widget.LatexFormulaWidget import LatexFormulaWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Приложение')
        self.setMinimumSize(400, 370)

        tabWidget = QTabWidget()


        tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        tabWidget.setMovable(True)

        self.tab_1 = QWidget()
        self.tab_2 = QWidget()

        tabWidget.addTab(self.tab_1, 'Вкладка 1')
        tabWidget.addTab(self.tab_2, 'Вкладка 2')

        tabWidget.setCurrentIndex(0)

        self.setCentralWidget(tabWidget)

        #Добавляем макет для первой вкладки
        layout_main_tab1 = QVBoxLayout()
        layout_main_tab1.setSpacing(0)
        #Устанавливает для вкладки tab_1 макет
        self.tab_1.setLayout(layout_main_tab1)

        # layout_main_tab1.addStretch()

        self.label_Title = QLabel('Типо таблица Д.3 СП16')
        self.label_Title.setStyleSheet('background-color: lightgreen')
        self.label_Title.setFixedHeight(100)




        layout_main_tab1.addWidget(self.label_Title)



        #СОЗДАНИЕ QLabel и QLineEdit
        #self.label_Flexibility = QLabel('гибкость:')
        self.label_Flexibility = LatexFormulaWidget(r'$\overline{\lambda}$', fontSize=20)
        #self.label_Flexibility = LatexFormulaWidget(r'$\sqrt[2]{\alpha}\gt x_{2}:dлл$')

        self.label_Flexibility.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        #self.label_Flexibility.set_latex_formula(r'$\overline{\lambda}$')


        #self.label_eccenticity = QLabel('Относительный эксцентриситет:')
        self.label_eccenticity = LatexFormulaWidget(r'$m_{ef}$', 'orange')
        #self.label_eccenticity.set_latex_formula(r'$m_{ef}$')

        #self.label_result = QLabel('Результат:')
        self.label_result = LatexFormulaWidget(r'$\varphi_{e}$')
        #self.label_result.set_latex_formula(r'$\varphi_{e}$')


        self.lineEdit_Flexibility = QLineEdit('2.5')
        self.lineEdit_Flexibility.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.lineEdit_Eccentricity = QLineEdit('15')
        self.lineEdit_Eccentricity.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.lineEdit_result = QLineEdit()
        self.lineEdit_result.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.lineEdit_result.setReadOnly(True)

        #Создание макета QGridLayout, в который поместим Qlabels и QLineEdits написанные выше
        gridLayout = QGridLayout()

        gridLayout.addWidget(self.label_Flexibility, 0, 0)
        gridLayout.addWidget(self.label_eccenticity, 1, 0)
        gridLayout.addWidget(self.label_result, 2, 0)

        gridLayout.addWidget(self.lineEdit_Flexibility, 0, 1)
        gridLayout.addWidget(self.lineEdit_Eccentricity, 1, 1)
        gridLayout.addWidget(self.lineEdit_result, 2, 1)

        gridLayout.setContentsMargins(0,0,0,0)
        gridLayout.setSpacing(0)

        #Установка columnStrech()
        gridLayout.setColumnStretch(0, 2)
        gridLayout.setColumnStretch(1, 8)

        #Добавляем макет gridLayout в макет layout_main_tab1
        layout_main_tab1.addLayout(gridLayout)
        layout_main_tab1.setContentsMargins(0,0,0,0)


        #Создание QLabel отвечающего за сообщения:
        self.label_Message = QLabel('Здесь будут сообщения')
        self.label_Message.setStyleSheet('background-color: red')
        self.label_Message.setFixedHeight(100)


        layout_main_tab1.addWidget(self.label_Message)


        #Создание QPushButton
        self.button_calculate = QPushButton('Расчитать')
        layout_main_tab1.addWidget(self.button_calculate)



        layout_main_tab2 = QVBoxLayout()
        self.tab_2.setLayout(layout_main_tab2)
        self.label_tab2 = QLabel('Лэйбл для второй страницы')
        layout_main_tab2.addWidget(self.label_tab2)


        #Привязка сигналов к слотам
        self.lineEdit_Flexibility.textChanged.connect(self.the_calculate)
        self.lineEdit_Eccentricity.textChanged.connect(self.the_calculate)

        self.the_calculate()

    def the_calculate(self):
        x = self.lineEdit_Eccentricity.text()
        print(x)
        y = self.lineEdit_Flexibility.text()
        print(y)
        if isNumberValue(x) and isNumberValue(y):


            result = findZ(listX, listY, listZ, float(x), float(y))
            if result != None:
                self.lineEdit_result.setText(str(round(result, 2)))
                self.label_Message.setText('Результат получен')

            else:
                self.label_Message.setText('Входные данные выходят за диапазон')
                self.lineEdit_result.setText('')
        else:
            self.label_Message.setText('Входные данные должны быть число')
            self.lineEdit_result.setText("")






app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()