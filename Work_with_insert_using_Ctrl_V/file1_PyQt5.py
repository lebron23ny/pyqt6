#https://ru.stackoverflow.com/questions/1386742/%D0%92%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%81%D0%BA%D0%BE%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%8F%D1%87%D0%B5%D0%B9%D0%BA%D0%B8-%D0%B8%D0%B7-excel-%D0%B2-%D1%8F%D1%87%D0%B5%D0%B9%D0%BA%D0%B8-qtablewidget
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.tableWidget = QTableWidget(3, 3, self.centralwidget)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.tableWidget)

        self.clipboard = QApplication.clipboard()

    def keyPressEvent(self, event):
        modifier = event.modifiers
        if event.modifiers() == Qt.ControlModifier:
            print('cntrl')


        if event.key() == Qt.Key_Shift:
            print('Шифт')
        if event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier:
            # Вручную обрабатывать данные буфера обмена и вставлять
            # их в таблицу, начиная с выбранного tableitem

            mime_data = self.clipboard.mimeData()
            # print(* mime_data.formats(), sep='\n')

            data = mime_data.data('application/x-qt-windows-mime;value="Csv"')
            #                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # Проверьте, содержит ли буфер обмена данные Excel.
            #  vvvv
            if data:
                # преобразовать из QByteArray в строку
                data = data.data().decode()

                list_item = data.split('\r')[0]
                list_item = list_item.split(';')
                # print(f'list_item = {list_item}')

                selectedIndexes = self.tableWidget.selectedIndexes()
                if selectedIndexes:
                    row = selectedIndexes[0].row()
                    column = selectedIndexes[0].column()
                    # print(f'row = {row}, column = {column}')

                    rows = self.tableWidget.rowCount()
                    columns = self.tableWidget.columnCount()
                    # print(f'rows = {rows}, columns = {columns}')

                    # проанализируйте данные и вставьте их в таблицу.
                    for item in list_item:
                        self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                        column += 1
                        if column >= columns:
                            break
                else:
                    msg = QMessageBox.information(
                        self,
                        'Внимание',
                        'Выберите ячейку, начиная с которой будите вставлять данные.'
                    )
            return
        super(MainWindow, self).keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(520, 320)
    w.show()
    sys.exit(app.exec_())