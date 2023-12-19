import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTableWidget, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        tableWidget = QTableWidget(6, 6)
        layout.addWidget(tableWidget)

        tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)


    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            print('Selected Cell Location Row: {0}, Columns: {1}'.format(ix.row(), ix.column()))

        for ix in deselected.indexes():
            print('Deselected Cell Location Row: {0}, Columns: {1}'.format(ix.row(), ix.column()))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    QWidget {
        font-size: 35px;
    }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')