import sys
# applicable to PyQt5 as well
from PyQt6.QtWidgets import QApplication, QTextEdit, QPushButton, QLineEdit, QLabel, QWidget, QHBoxLayout, QVBoxLayout

"""
Example Iterating Child Widgets
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1000, 800
        self.setMinimumSize(self.window_width, self.window_height)

        self.textEdit = QTextEdit(self)
        self.textEdit.resize(1200, 400)

        self.label = QLabel('Label Widget', self)
        self.label.move(70, 450)

        self.layout = QVBoxLayout(self)
        # self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.button1 = QPushButton('Button 1', clicked=self.listchildWidgets)
        self.button2 = QPushButton('Button 2', clicked=self.listChildWidget)
        self.button3 = QPushButton('Button 3', clicked=self.listLayoutChildWidgets)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

    def listchildWidgets(self):
        print(self.findChildren(QWidget))
        print(self.findChildren(QPushButton))
        print(self.layout.findChildren(QPushButton))

    def listChildWidget(self):
        print(self.findChild(QWidget).toPlainText())

    def listLayoutChildWidgets(self):
        # print(self.layout.findChild(QWidget))
        for i in range(self.layout.count()):
            print(self.layout.itemAt(i).widget().text())
            # print(self.layout.itemAt(i).widget().objectName())


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')