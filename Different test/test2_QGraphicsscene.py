from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QFrame, QLabel, \
    QGraphicsScene, QGraphicsView, QGraphicsRectItem
import sys

class MyView(QGraphicsView):
    def __init__(self, parent=None):
        QGraphicsView.__init__(self, parent=parent)
        self.scene = QGraphicsScene(self)
        self.item = QGraphicsRectItem(300, 400, 100, 100)
        self.scene.addItem(self.item)
        self.setScene(self.scene)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(50, 50, 900, 700)
        self.setWindowTitle("Pre-Alignment system")
        widget = QWidget()

        # create the view
        self.view = MyView()
        self.label = QLabel("Label")
        self.label.setStyleSheet('color: white;'
                                 'font-weight:bold;'
                                 'font-size:20pt;'
                                 'background-color:lightgreen;'
                                 'border: 2px solid black;'
                                 'border-radius:10px')
        vbox = QVBoxLayout()
        vbox.addWidget(self.view)
        vbox.addWidget(self.label)
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
