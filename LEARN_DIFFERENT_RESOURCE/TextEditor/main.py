## https://www.youtube.com/watch?v=eipstdomHQE&list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&index=6

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Редактор кода')
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu('&Файл',self)
        self.menuBar.addMenu(fileMenu)

        open_file = fileMenu.addMenu('&Открыть')
        open_file.addAction('Открыть что-то', self.action_clicked)
        #open_file_all = open_file.addMenu('&Открыть все')

        fileMenu.addAction('Сохранить',self.action_clicked)
        fileMenu.addAction('Закрыть',self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Закрыть':
            print('Close')
            self.close()
        elif action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('')


        elif action.text() == 'Открыть что-то':
            fname = QFileDialog.getOpenFileName(self)[0]

            print('Открыть что-то')
            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print('Не выбран файл')


        #print('Action: ' + action.text())

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    application()
