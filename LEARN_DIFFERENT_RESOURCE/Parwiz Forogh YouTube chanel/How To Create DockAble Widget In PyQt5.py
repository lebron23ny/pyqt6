# https://www.youtube.com/watch?v=gGIlLOqRBs4
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDockWidget, QTextEdit, QListWidget, QPushButton, QWidget,
                             QVBoxLayout)
import sys
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QObject
from PyQt6.uic.properties import QtCore


class DockDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'PyQt6 Dock'
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createDockWidget()
        self.BindingSignal()

        self.show()

    def createDockWidget(self):
        menubar = self.menuBar()
        file = menubar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('Close')
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.textEdit = QTextEdit()
        self.textEdit.setText("")
        self.button = QPushButton()
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.button)

        self.textEdit.setPlaceholderText('Выберите язык')

        self.dock_right = QDockWidget('Dockable right', self)
        self.listwidget_dock_right = QListWidget()
        list = ['Python', 'C++', 'Java', 'C#']
        for el in list:
            self.listwidget_dock_right.addItem(el)

        self.dock_right.setWidget(self.listwidget_dock_right)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock_right)

        self.dock_left = QDockWidget('Dockable left', self)
        self.listwidget_dock_left = QListWidget()
        list_left = ['Пн', 'Вт']
        for el in list_left:
            self.listwidget_dock_left.addItem(el)

        self.dock_left.setWidget(self.listwidget_dock_left)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_left)

    def BindingSignal(self):
        self.listwidget_dock_right.itemSelectionChanged.connect(self.selectionChanged)
        self.listwidget_dock_left.itemSelectionChanged.connect(self.selectionChanged)
        self.button.clicked.connect(self.btn_click)

    def selectionChanged(self):
        listwidget = self.sender()  # Получаем объект listWidget который отправил сигнал
        index = listwidget.currentIndex().row()
        text_old = self.textEdit.toPlainText()
        text_selected = listwidget.currentItem().text()
        # text = text_old + listwidget.item(index).text()
        text = text_old + text_selected

        self.textEdit.setText(text + '\n')

    # def selectionChanged(self):
    #     index = self.listwidget_dock_right.currentIndex().row()
    #     text_old = self.textEdit.toPlainText()
    #     text = text_old + self.listwidget_dock_right.item(index).text()
    #
    #     self.textEdit.setText(text + '\n')

    def btn_click(self):
        print(self.listwidget_dock_right.count())


App = QApplication(sys.argv)
window = DockDialog()
sys.exit(App.exec())
