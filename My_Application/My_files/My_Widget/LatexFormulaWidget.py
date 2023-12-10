import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class LatexFormulaWidget(QFrame):
    def __init__(self, formula, colorBackground='yellow', fontSize=10):
        super(LatexFormulaWidget, self).__init__()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)



        self.__latex_formula = formula

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)


        self.setLayout(layout)
        self.set_latex_formula(self.__latex_formula, colorBackground, fontSize)
        # self.setStyleSheet('border: 2px solid black;'
        #                     )

    def set_latex_formula(self, formula, colorBackground, fontSize):

        self.__latex_formula = formula
        self.figure.clear()
        self.figure.set_size_inches(1,0.25)
        self.figure.set_facecolor(colorBackground)


        ax = self.figure.add_subplot(111)
        ax.text(0.5, 0.5, formula, size=fontSize, ha='center', va='center')
        ax.axis('off')
        self.canvas.draw()

    def get_latex_formula(self):
        return self.__latex_formula


