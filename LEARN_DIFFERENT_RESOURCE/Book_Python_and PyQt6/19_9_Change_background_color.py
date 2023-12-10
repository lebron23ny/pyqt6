from PyQt6 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Изменение цвета фона окна')
window.resize(300, 100)
pal = window.palette()
pal.setColor(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window, QtGui.QColor('blue'))
pal.setColor(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, QtGui.QColor('#ff0000'))
window.setPalette(pal)
label = QtWidgets.QLabel('Текст надписи')
label.setStyleSheet('background-color: #ffffff;')
label.setAutoFillBackground(True)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
app.exec()