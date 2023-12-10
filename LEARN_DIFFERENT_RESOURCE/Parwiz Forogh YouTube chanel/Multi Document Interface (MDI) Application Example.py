#https://www.youtube.com/watch?v=zw9irXRG-9c
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QDockWidget, QWidget, \
    QVBoxLayout, QListWidget, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class SubWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout_sub_widget = QVBoxLayout()
        self.setLayout(layout_sub_widget)
        label_sub = QLabel('Label 1')
        textEdit_sub = QLineEdit()
        listWidget_sub = QListWidget()
        listWidget_sub.addItem('ПН')
        listWidget_sub.addItem('ВТ')
        listWidget_sub.addItem('СР')
        listWidget_sub.addItem('ЧТ')
        listWidget_sub.addItem('ПТ')
        listWidget_sub.addItem('СБ')
        listWidget_sub.addItem('ВС')
        button_sub = QPushButton('Click')
        layout_sub_widget.addWidget(label_sub)
        layout_sub_widget.addWidget(textEdit_sub)
        layout_sub_widget.addWidget(listWidget_sub)
        layout_sub_widget.addWidget(button_sub)


class MDIWindow(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()




        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Cascade')
        file.addAction('Tiled')
        file.triggered[QAction].connect(self.WindowTrig)

        dockWidget = QDockWidget('Dock', self)
        self.widget_Dock = QWidget()
        self.layout_Dock = QVBoxLayout()
        self.listWidget = QListWidget()
        self.listWidget.addItem('Google')
        self.listWidget.addItem('Facebook')
        self.listWidget.addItem('Miscroft')
        self.listWidget.addItem('Apple')
        self.button = QPushButton('click')
        self.layout_Dock.addWidget(self.listWidget)
        self.layout_Dock.addWidget(self.button)
        self.widget_Dock.setLayout(self.layout_Dock)
        dockWidget.setWidget(self.widget_Dock)
        dockWidget.setFloating(False)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dockWidget)

        self.setWindowTitle('MDI Application')

    def WindowTrig(self, p):
        if p.text() == 'New':
            MDIWindow.count = MDIWindow.count + 1
            sub = QMdiSubWindow()

            subWidget = SubWidget()



            sub.setWidget(subWidget)
            sub.setWindowTitle('Sub Window ' + str(MDIWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        if p.text() == 'Cascade':
            self.mdi.cascadeSubWindows()

        if p.text() == 'Tiled':
            self.mdi.tileSubWindows()



app = QApplication(sys.argv)
mdiwindow = MDIWindow()
mdiwindow.show()
app.exec()

