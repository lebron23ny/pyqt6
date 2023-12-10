from PyQt6 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Изoбpaжeни e  в  качестве  фона")
window.resize(300, 100)
pal = window.palette()
pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap('Icons/ENERGOPROECT_LOGO.png')))
window.setPalette(pal)

label = QtWidgets.QLabel("Текст надписи")
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label.setStyleSheet('background-image: url(Icons/ibeam_icon.png);')
label.setAutoFillBackground(True)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)




window.show()
app.exec()