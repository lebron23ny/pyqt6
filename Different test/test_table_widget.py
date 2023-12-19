import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QVBoxLayout, QPushButton, QTableView, \
    QTableWidgetItem, QHeaderView, QMainWindow, QStyledItemDelegate, QStyle

from PyQt6.QtGui import QClipboard, QGuiApplication, QShortcut, QKeySequence






class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()
        self.SetStyleMyWindow()
        self.BindingSignal()
        self.InitShortCut()


        self.clipboard = QGuiApplication.clipboard()

    def InitUI(self):
        layout = QVBoxLayout()

        self.table_widget = QTableWidget(5, 3)
        self.table_widget.setHorizontalHeaderLabels(['N, kN', 'Q, kN', 'M, kN*m'])
        self.btn_add_row = QPushButton('Добавить строку')
        self.btn_delete_row = QPushButton('Удалить строку')
        self.btn_get_value = QPushButton('Получить значение')
        self.btn_set_value = QPushButton('Установить значение')
        self.btn_get_count_row_and_column = QPushButton('Получить кол-во строк и столбцов')
        self.btn_get_header_current_row = QPushButton('Получить заголовок выбранной ячейки')
        self.btn_insert_from_clipboard = QPushButton('Вставить из буфера обмена')
        self.btn_get_selected_ranges = QPushButton('Получить диапазон выбранных ячеек')

        layout.addWidget(self.table_widget)
        layout.addWidget(self.btn_add_row)
        layout.addWidget(self.btn_delete_row)
        layout.addWidget(self.btn_get_value)
        layout.addWidget(self.btn_set_value)
        layout.addWidget(self.btn_get_count_row_and_column)
        layout.addWidget(self.btn_get_header_current_row)
        layout.addWidget(self.btn_insert_from_clipboard)
        layout.addWidget(self.btn_get_selected_ranges)

        self.setLayout(layout)

    def SetStyleMyWindow(self):
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setMinimumSize(500, 400)
        # Чтобы ширина столбцов заполняло все пространство таблицы
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


        # Скрыть вертикальные заголовки
        #self.table_widget.verticalHeader().setVisible(False)





        self.setObjectName('mainWidget')
        self.btn_add_row.setObjectName('btnStyle1')
        self.btn_delete_row.setObjectName('btnStyle1')





    def BindingSignal(self):
        self.btn_add_row.clicked.connect(self.btn_add_click)
        self.btn_delete_row.clicked.connect(self.btn_delete_click)
        self.btn_get_value.clicked.connect(self.btn_get_value_click)
        self.btn_set_value.clicked.connect(self.btn_set_value_click)
        self.btn_get_count_row_and_column.clicked.connect(self.btn_get_count_row_and_column_click)
        self.btn_get_header_current_row.clicked.connect(self.btn_get_header_current_row_click)
        self.btn_insert_from_clipboard.clicked.connect(self.btn_insert_from_clipboard_click)
        self.btn_get_selected_ranges.clicked.connect(self.btn_get_selected_ranges_click)

    def InitShortCut(self):
        self.shortcut = QShortcut(QKeySequence('Ctrl+V'), self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.shortcut_method(shortcut_key))

        self.shortcut = QShortcut(QKeySequence.StandardKey.Delete, self)
        self.shortcut.activated.connect(
            lambda shortcut_key=self.shortcut.key().toString(): self.shortcut_method(shortcut_key))

    def btn_add_click(self):
        count_Row = self.table_widget.rowCount()
        self.table_widget.setRowCount(count_Row + 1)

    def btn_delete_click(self):
        count_Row = self.table_widget.rowCount()
        self.table_widget.setRowCount(count_Row - 1)

    def btn_get_value_click(self):
        currentItem = self.table_widget.currentItem()
        currentRow = self.table_widget.currentRow()
        currentColumn = self.table_widget.currentColumn()
        if currentItem is not None:
            currentText = currentItem.text()
            currentRow = currentItem.row()
            currentColumn = currentItem.column()
            print('Значение: {0}'.format(currentText))
            print('Ряд: {}'.format(currentRow))
            print('Колонна: {}'.format(currentColumn))
            print()
        else:
            print('не выбраны ячейки или они пустые')
            print('Ряд: {}'.format(currentRow))
            print('Колонна: {}'.format(currentColumn))
            print()

    def btn_set_value_click(self):
        item = QTableWidgetItem('fff')
        #Выравнивание по центру
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.table_widget.setItem(2, 2, item)

    def btn_get_count_row_and_column_click(self):
        rowsCount = self.table_widget.rowCount()
        columnsCount = self.table_widget.columnCount()
        print('Количество рядов: {0}'.format(rowsCount))
        print('Количество столбцов: {0}'.format(columnsCount))

    def btn_get_header_current_row_click(self):
        headers = self.table_widget.horizontalHeaderItem(0)
        text = headers.text()
        print(text)
        a = 0

    def btn_insert_from_clipboard_click(self):
        text = self.clipboard.text()
        data = [s for s in text.split('\n') if s.strip() != '']
        data_list = [el.split('\t') for el in data]
        print(data)
        print(data_list)

    def btn_get_selected_ranges_click(self):
        print('Выбранные индексы: ')
        selectedIndexes = self.table_widget.selectedIndexes()
        for item in selectedIndexes:
            print('Выбранные индексы: ', item.row(), item.column())

    def shortcut_method(self, mapping):

        if mapping == 'Ctrl+V':
            text = self.clipboard.text()
            data = self.parse_clipboard(text)
            startRow = self.table_widget.currentRow()
            startColumn = self.table_widget.currentColumn()
            ind_row = 0
            for row_data in data:
                ind_column = 0
                for column in row_data:
                    self.table_widget.setItem(startRow + ind_row,
                                              startColumn + ind_column,
                                              QTableWidgetItem(data[ind_row][ind_column]))
                    ind_column += 1
                ind_column = 0
                ind_row += 1
        elif mapping == 'Del':

            selectedIndexes = self.table_widget.selectedIndexes()
            for item in selectedIndexes:
                self.table_widget.setItem(item.row(), item.column(), QTableWidgetItem(''))

    def parse_clipboard(self, text):
        data = [s for s in text.split('\n') if s.strip() != '']
        data_list = [el.split('\t') for el in data]
        return data_list


app = QApplication(sys.argv)


StylesSheet = '''
QWidget#mainWidget {
    background-color: green;
    }
        
        
QTableWidget{
     background: silver; 
     border:2px solid black;
     font-size: 12px; 
     font-family:"Microsoft YaHei";
     color:blue; 
     border-radius:0px
    }
QTableWidget::item
{
    
}

QTableWidget::item::selected
{
    color:red; 
    border: none;
    outline: none;
    background: green;
}
QTableWidget::item:selected:focus 
{
    border: none;
    outline: none;
    background-color: green
}


  
    
QPushButton#btnStyle1 {
    color: white;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
}
QPushButton#btnStyle1:hover {
    color: black;
    background-color: gold;
    font-weight:bold; 
}
QPushButton#btnStyle1:pressed {
    color: gold;
    background-color: red;
    
}

'''
app.setStyleSheet(StylesSheet)



win = MyWindow()
win.show()

app.exec()
