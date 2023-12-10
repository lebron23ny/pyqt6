import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QLabel, QLineEdit, QVBoxLayout,
                             QGridLayout, QHBoxLayout, QSizePolicy)
from PyQt6.QtGui import QIcon


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



from My_Library.Calculate import findZ, isNumberValue
from My_Library.Calculate import listX, listY, listZ

from My_Widget.LatexFormulaWidget import LatexFormulaWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitializeComponent()

        self.BindingSignal()

        self.SetStyle()






        self.the_calculate()

    def InitializeComponent(self):

        self.tabWidget = QTabWidget()
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tabWidget.addTab(self.tab_1, 'Вкладка 1')
        self.tabWidget.addTab(self.tab_2, 'Вкладка 2')

        self.setCentralWidget(self.tabWidget)


        self.label_Title_Window = QLabel('Приложение 1')

        self.button_close = QPushButton('х')

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.label_Title_Window)
        hLayout.addWidget(self.button_close)

        self.label_Title = QLabel('Типо таблица Д.3 СП16')
        # СОЗДАНИЕ QLabel и QLineEdit
        self.label_Flexibility = LatexFormulaWidget(r'$\overline{\lambda}$', fontSize=16)
        self.label_eccenticity = LatexFormulaWidget(r'$m_{ef}$', 'orange', fontSize=16)
        self.label_result = LatexFormulaWidget(r'$\varphi_{e}$', fontSize=16)
        self.lineEdit_Flexibility = QLineEdit('2.5')
        self.lineEdit_Eccentricity = QLineEdit('15')
        self.lineEdit_result = QLineEdit()


        #Создаем label_Message и button_Calculate
        self.label_Message = QLabel('Здесь будут сообщения')
        self.button_calculate = QPushButton('Расчитать')

        # Созданем макет QGridLayout, в который поместим Qlabels и QLineEdits написанные выше
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.label_Flexibility, 0, 0)
        gridLayout.addWidget(self.label_eccenticity, 1, 0)
        gridLayout.addWidget(self.label_result, 2, 0)

        gridLayout.addWidget(self.lineEdit_Flexibility, 0, 1)
        gridLayout.addWidget(self.lineEdit_Eccentricity, 1, 1)
        gridLayout.addWidget(self.lineEdit_result, 2, 1)

        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(0)
        # Установка columnStrech()
        gridLayout.setColumnStretch(0, 2)
        gridLayout.setColumnStretch(1, 8)

        


        # Создаем макет для первой вкладки
        layout_main_tab1 = QVBoxLayout()
        layout_main_tab1.setSpacing(0)

        # Добавляем в макет layout_main_tab1 hLayout
        layout_main_tab1.addLayout(hLayout)

        #Добавляем в макет layout_main_tab1 label_Title
        layout_main_tab1.addWidget(self.label_Title)

        # Добавляем макет gridLayout в макет layout_main_tab1
        layout_main_tab1.addLayout(gridLayout)
        layout_main_tab1.setContentsMargins(0, 0, 0, 0)

        #Добавляем в макет layout_main_tab1 label_Message
        layout_main_tab1.addWidget(self.label_Message)
        #Добавляем в макет layout_main_tab1 button_calculate
        layout_main_tab1.addWidget(self.button_calculate)


        self.tab_1.setLayout(layout_main_tab1)

        layout_main_tab2 = QVBoxLayout()
        layout_main_tab2.setContentsMargins(0, 0, 0, 0)
        self.tab_2.setLayout(layout_main_tab2)
        self.label_tab2 = QLabel('Лэйбл для второй страницы')
        layout_main_tab2.addWidget(self.label_tab2)


    def BindingSignal(self):
        # Привязка сигналов к слотам
        self.lineEdit_Flexibility.textChanged.connect(self.the_calculate)
        self.lineEdit_Eccentricity.textChanged.connect(self.the_calculate)
        self.button_close.clicked.connect(self.the_close)


    def SetStyle(self):
        self.setWindowIcon(QIcon('ENERGOPROECT_LOGO.png'))
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)


        self.label_Title_Window.setFixedHeight(30)
        self.button_close.setFixedWidth(30)
        self.button_close.setFixedHeight(30)
        self.button_close.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.label_Title_Window.setStyleSheet('color: black;'
                                                'font-size:16pt;'
                                                'border: 2px solid black;'
                                                'background-color:red;'
                                                'font-weight: bold;'
                                                'padding-left:10px;')


        self.button_close.setStyleSheet((
                                            'QPushButton'
                                                '{'
                                                'text-align: center;'
                                                'color:white;'
                                                'font-size:15pt;'
                                                'font-weight:bold;'
                                                'background-color:red;'
                                                'border: 2px solid black;'
                                                'border-radius:5px;'
                                                'width:230px;'
                                                'height:50px;'
                                               
                                                '}'
                                            'QPushButton:hover'
                                                '{'
                                                'background-color:blue;'
                                                '}'
                                            'QPushButton:pressed'
                                                '{'
                                                'background-color:green;'
                                                '}'))




        # self.setStyleSheet('font-weight:bold;'
        #                    'font-size:20pt;')
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)

        self.tabWidget.setStyleSheet('color: black;'
                                 'font-size:10pt;'
                                 'border: 1px solid black;'
                                 'font-weight: bold;'
                                 )


        self.setWindowTitle('Приложение №1')
        self.setMinimumSize(550, 370)
        self.label_Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Title.setStyleSheet('color: white;'
                                       'font-weight:bold;'
                                       'font-size:20pt;'
                                       'background-color:lightgreen;'
                                       'border: 2px solid black;'
                                       'border-radius:10px')
        self.label_Title.setFixedHeight(100)
        self.lineEdit_Flexibility.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.lineEdit_Flexibility.setPlaceholderText('Введите гибкость')
        self.lineEdit_Flexibility.setStyleSheet('color: black;'
                                                'font-size:16pt;'
                                                'border: 2px solid black;'
                                                #'border-radius:10px;'
                                                'font-weight: bold;'
                                                'padding-left:10px;'
                                                )


        self.lineEdit_Eccentricity.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.lineEdit_Eccentricity.setPlaceholderText('Введите эксцентриситет')
        self.lineEdit_Eccentricity.setStyleSheet('color: black;'
                                                'border: 2px solid black;'
                                                 #'border-radius:10px;'
                                                'font-size:16pt;'
                                                
                                                'font-weight: bold;'
                                                'padding-left:10px;')

        self.lineEdit_result.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.lineEdit_result.setReadOnly(True)
        self.lineEdit_result.setPlaceholderText('Результат')


        self.lineEdit_result.setStyleSheet('color: black;'
                                                'font-size:16pt;'
                                                'border: 2px solid black;'
                                                 #'border-radius:10px;'
                                                'font-weight: bold;'
                                                'padding-left:10px;')

        self.label_Message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Message.setStyleSheet('color: white;'
                                         'font-weight:bold;'
                                         'font-size:20pt;'
                                         'background-color:none;'
                                         'border:none;'
                                         'border: 2px solid black;'
                                         'background-color:lightgreen;'
                                         'border-radius:10px;')
        self.label_Message.setFixedHeight(100)

        self.button_calculate.setStyleSheet(
                                            'QPushButton'
                                                '{'
                                                'color:white;'
                                                'font-size:20pt;'
                                                'font-weight:bold;'
                                                'background-color:red;'
                                                'border: 2px solid black;'
                                                'border-radius:10px;'
                                                'width:230px;'
                                                'height:50px;'
                                               
                                                '}'
                                            'QPushButton:hover'
                                                '{'
                                                'background-color:blue;'
                                                '}'
                                            'QPushButton:pressed'
                                                '{'
                                                'background-color:green;'
                                                '}')
        self.label_Flexibility.parent().setStyleSheet('border: 2px solid black;')
        self.label_eccenticity.parent().setStyleSheet('border: 2px solid black;')
        self.label_result.parent().setStyleSheet('border: 2px solid black;')








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


    def the_close(self):
        self.close()






app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()