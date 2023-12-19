import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFont


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700, 100)
        mainLayout = QHBoxLayout()
        self.model = QStandardItemModel()

        self.comboStates = QComboBox()
        self.comboStates.setFixedSize(325, 50)
        self.comboStates.setFont(QFont('', 12))
        self.comboStates.setModel(self.model)

        self.comboCities = QComboBox()
        self.comboCities.setFixedSize(325, 50)
        self.comboCities.setFont(QFont('', 12))
        self.comboCities.setModel(self.model)

        mainLayout.addWidget(self.comboStates)
        mainLayout.addWidget(self.comboCities)

        self.setLayout(mainLayout)


        for k, v in data.items():
            state = QStandardItem(k)
            self.model.appendRow(state)
            for value in v:
                city = QStandardItem(value)
                state.appendRow(city)



        self.comboStates.currentIndexChanged.connect(self.updateStateCombo)
        self.updateStateCombo(0)

        self.comboStates.currentTextChanged.connect(self.current_text_change)


    def updateStateCombo(self, index):
        indx = self.model.index(index, 0, self.comboStates.rootModelIndex())
        self.comboCities.setRootModelIndex(indx)
        self.comboCities.setCurrentIndex(0)

    def current_text_change(self, text):
        print(text)





data = {'California': ['San Francisco', 'Okland', 'Los Angeles'],
        'Illinois': ['Chicago', 'Sprinfield', 'Evanston'],
        'Texas': ['Austin', 'Houston', 'San Antonio']}

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec())