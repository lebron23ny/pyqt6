import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QApplication


class CheckList(QListWidget):
    def __init__(self, strings, parent=None):
        super().__init__(parent)
        for text in strings:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.addItem(item)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    view = CheckList(["item 1", "item 2", "item 3", "item 4", "item 5"])
    view.show()
    sys.exit(app.exec())
