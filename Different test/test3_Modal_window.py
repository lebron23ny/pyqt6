from PyQt6 import QtCore, QtWidgets
import sys


def show_modal_window():
    global modalWindow
    modalWindow = QtWidgets.QWidget(window1, QtCore.Qt.WindowТype.Window)
    modalWindow.setWindowТitle("Moдaльнoe  окно")
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowМodality.WindowМodal)
    modalWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, True)
    modalWindow.move(window1.geometry().center() -
                     modalWindow.rect().center() - QtCore.QPoint(4, 30))
    modalWindow.show()


арр = QtWidgets.QApplication(sys.argv)
window1 = QtWidgets.QWidget()
window1.setWindowTitle('Обычное окно')
window1.resize(300, 100)
button = QtWidgets.QPushButton("Oткpыт ь  модальное  окно")
button.clicked.connect(show_modal_window)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
window1.setLayout(vbox)
window1.show()
window2 = QtWidgets.QWidget()
window2.setWindowTitle("Этo  окно  не  будет  блокир овано")
window2.resize(500, 100)
window2.show()
