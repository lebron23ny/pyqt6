from PySide6 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar
import sys

app = QtWidgets.QApplication([])
volume = PowerBar()
volume.show()
app.exec()