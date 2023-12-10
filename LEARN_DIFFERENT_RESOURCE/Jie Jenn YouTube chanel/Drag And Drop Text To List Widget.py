import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QListView, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class ListView(QListView):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setModel(QStandardItemModel(0, 1))

    def dragEnterEvent(self, e):
        d = e.accept()
        type = e.type()
        type1 = QEvent.Type.DragEnter
        ss = e.mimeData().hasText()
        e.accept() if e.mimeData().hasText() else e.ignore()

    def dragMoveEvent(self, e):
        e.accept() if e.mimeData().hasText() else e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasText():
            e.setDropAction(Qt.DropAction.CopyAction)
            self.model().appendRow(QStandardItem(e.mimeData().text()))
            e.accept()
        else:
            e.ignore()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QHBoxLayout()
        self.setLayout(layout)

        textEdit = QTextEdit()
        textEdit.setText('dsdsssdsdsdsds\n1234455')
        listView = ListView()



        layout.addWidget(textEdit)
        layout.addWidget(listView)


if __name__ == '__main__':
    app =QApplication(sys.argv)
    app.setStyleSheet('''
    Qwidget {
    font-size: 30px;
    ''')
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')