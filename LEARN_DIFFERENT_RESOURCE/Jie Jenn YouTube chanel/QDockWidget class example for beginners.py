import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget, QPushButton, QWidget,
                             QVBoxLayout)
from PyQt5.QtCore import Qt





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)


        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFontPointSize(16)

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
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget)


        self.listWidget.itemDoubleClicked.connect(self.get_list_item)

    def get_list_item(self):
        self.textEdit.setPlainText(self.listWidget.currentItem().text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())