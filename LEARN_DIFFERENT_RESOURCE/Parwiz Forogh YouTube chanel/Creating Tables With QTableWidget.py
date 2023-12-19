#https://www.youtube.com/watch?v=ECIZgWeyFFk
import sys

from PyQt6.QtWidgets import QWidget, QTableWidget, QApplication, QVBoxLayout, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(300, 400)

        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)

        self.table_widget.setItem(0, 0, QTableWidgetItem('Name'))
        self.table_widget.setItem(0, 1, QTableWidgetItem('Email'))
        self.table_widget.setItem(0, 2, QTableWidgetItem('Phone No'))

        self.table_widget.setItem(1, 0, QTableWidgetItem('John'))
        self.table_widget.setItem(1, 1, QTableWidgetItem('John@gmail.com'))
        self.table_widget.setItem(1, 2, QTableWidgetItem('8748484'))

        self.table_widget.setItem(2, 0, QTableWidgetItem('John'))
        self.table_widget.setItem(2, 1, QTableWidgetItem('John@gmail.com'))
        self.table_widget.setItem(2, 2, QTableWidgetItem('8748484'))




        self.setLayout(layout)



app = QApplication(sys.argv)
wind = MyWidget()
wind.show()

app.exec()

