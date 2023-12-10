#https://ru.stackoverflow.com/questions/1386742/%D0%92%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%81%D0%BA%D0%BE%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%8F%D1%87%D0%B5%D0%B9%D0%BA%D0%B8-%D0%B8%D0%B7-excel-%D0%B2-%D1%8F%D1%87%D0%B5%D0%B9%D0%BA%D0%B8-qtablewidget
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QTableWidget, QMainWindow, QGridLayout, QApplication, QTableWidgetItem, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.tableWidget = QTableWidget(3, 3, self.centralwidget)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.tableWidget)

        self.clipoard = QApplication.clipboard()

    def keyPressEvent(self, event):
        k = event.key()
        k1 = Qt.Key.Key_C
        modifiers = event.modifiers()
        type1 = type(event)
        name = modifiers.name

        # if event.key() == Qt.Key.Key_C:
        #     print('Нажата С')
        #
        # if event.modifiers() == Qt.Modifier.CTRL:
        #     print('нажат ctrl')
        #
        # if event.modifiers() == Qt.Modifier.ALT:
        #     print('нажат Alt')

        if event.modifiers() == Qt.Modifier.MODIFIER_MASK:
            print('удерживается Ctrl')

        if event.key() == Qt.Key.Key_Shift:
            print('shift press')

        if event.key() == Qt.Key.Key_Shift:
            print('ctrl')

        if event.key() == Qt.Key.Key_C and event.modifiers().name == 'ControlModifier':
            print('ctrl+C')




        # if event.key() == Qt.Key.Key_C:
        #     print('Нажата кнопка C')
        super(MainWindow, self).keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(520, 320)
    w.show()
    app.exec()