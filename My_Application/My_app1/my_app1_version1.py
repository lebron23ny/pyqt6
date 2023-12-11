import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt6 import QtCore


from _My_Library.My_Function.Calculate import findZ, isNumberValue
from _My_Library.My_Function.Calculate import listX, listY, listZ



import numpy as np

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение")
        #self.setGeometry(50, 50, 300, 350)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)

        #Размеры приложения, если размеры окно
        # self.setFixedSize(300, 350)

        #СОЗДАНИЕ ВКЛАДОК
        #Создание TabWidget
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 300, 350))
        self.tabWidget.setObjectName("tabWidget")

        #Создание вкладки 1 и вкладки 2
        self.tab_1 = QWidget()
        #self.tab_1.setObjectName("tab1")


        self.tab_2 = QWidget()
        #self.tab_2.setObjectName("tab_2")


        #Добавление вкладки 1 и 2 в TabWidget
        self.tabWidget.addTab(self.tab_1, "Вкладка 1")
        self.tabWidget.addTab(self.tab_2, "Вклдака 2")

        #Установка текущей вкладки
        self.tabWidget.setCurrentIndex(0)

        #привязка сигнала currentChanged объекта TabWidget к слоту the_current_index
        self.tabWidget.currentChanged.connect(self.the_current_index)


        #СОЗДАНИЕ ОБЪЕКТОВ QLABEL

        self.label_Title = QLabel('Типо таблица Д.3 СП16')
        self.label_Title.setGeometry(10, 10, 180,40)
        self.label_Title.setParent(self.tab_1)


        self.label_Flexibility = QLabel('гибкость:')
        self.label_Flexibility.setGeometry(10, 50, 180, 40)
        #Добавляем эту штуковину во вкладку 1
        self.label_Flexibility.setParent(self.tab_1)

        self.label_eccenticity = QLabel()
        self.label_eccenticity.setText('Относительный эксцентриситет:')
        self.label_eccenticity.setGeometry(10, 120, 180, 40)
        self.label_eccenticity.setParent(self.tab_1)

        self.label_result = QLabel()
        self.label_result.setText('Результат:')
        self.label_result.setGeometry(10, 190, 180, 40)
        self.label_result.setParent(self.tab_1)

        self.label_Message = QLabel('Здесь будут сообщения')
        self.label_Message.setGeometry(10, 240, 220, 40)
        self.label_Message.setParent(self.tab_1)


        #СОЗДАНИЕ ОБЪЕКТОВ QLINEEDIT

        self.lineEdit_Flexibility = QLineEdit('2.5')
        self.lineEdit_Flexibility.setGeometry(210, 50, 50, 40)
        self.lineEdit_Flexibility.setPlaceholderText("Enter your text")
        self.lineEdit_Flexibility.setParent(self.tab_1)


        #Привязка сигнала textChanged к слоту the_calculate
        self.lineEdit_Flexibility.textChanged.connect(self.the_calculate)

        self.lineEdit_Eccentricity = QLineEdit('15')
        self.lineEdit_Eccentricity.setGeometry(210, 120, 50, 40)
        self.lineEdit_Eccentricity.setPlaceholderText("Enter your text")
        self.lineEdit_Eccentricity.setParent(self.tab_1)

        self.lineEdit_Eccentricity.textChanged.connect(self.the_calculate)

        self.lineEdit_result = QLineEdit()
        self.lineEdit_result.setGeometry(210, 190, 50, 40)
        self.lineEdit_result.setPlaceholderText("Result")

        #Устанавливаем свойсвто для этого QLineEdit - Только для чтения
        self.lineEdit_result.setReadOnly(True)
        self.lineEdit_result.setParent(self.tab_1)





        self.button_calculate = QPushButton('Расчитать')
        self.button_calculate.setGeometry(90, 280, 75, 25)
        self.button_calculate.setParent(self.tab_1)


        self.button_calculate.clicked.connect(self.the_calculate)



        #ЭТА ШТУКОВИНА ДОБАВЛЯЕТ ГРАФИК НА ВТОРОЙ ЛИСТ
        self.widget = QWidget()
        self.widget.setParent(self.tab_2)

        layot = QVBoxLayout()
        self.widget.setLayout(layot)


        canvas = FigureCanvasQTAgg(fig)


        layot.addWidget(canvas)




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
                print(result)
            else:
                self.label_Message.setText('Входные данные выходят за диапазон')
                self.lineEdit_result.setText('')
        else:
            self.label_Message.setText('Входные данные должны быть число')
            self.lineEdit_result.setText("")


    def the_current_index(self, index):
        print(f'Текущий индекс вкладки {index}')
        name_tab = self.tabWidget.tabText(index)
        print(name_tab)



x = np.array(listX)
y = np.array(listY)
z = np.array(listZ)

X, Y = np.meshgrid(x, y)
fig = Figure(figsize=(4, 3), dpi=80)

ax = fig.add_subplot(111, projection = '3d')

surf = ax.plot_surface(X, Y, z, cmap='viridis')

ax.set_xlabel('$m_{ef}$')
#ax.set_ylabel(r'$\lambda$')
ax.set_ylabel(r'$\overline{\lambda}$')
ax.set_zlabel('$φ_{ex}$')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# x = [1, 2, 8, 3, 6]
# y = [9, 3, 1, 6, 3]
#
#
# fig = Figure()
# ax = fig.add_subplot()
# ax.plot(x, y)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()