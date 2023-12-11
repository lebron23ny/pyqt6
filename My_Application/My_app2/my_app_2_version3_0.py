from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QComboBox, QVBoxLayout, QGridLayout,
                             QTextEdit, QPushButton, QSizePolicy)
from PyQt6.QtCore import Qt

from _My_Library.My_Function.Pixmap_Latex import mathTex_to_QPixmap
import sys
import sqlite3
from _My_Library.My_Widget.My_custom_title_bar import MyCustomTittleBar

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('my_database.db')
        self.cursor = self.connection.cursor()

        self.InitializeComponent()
        self.SetValuesDefault()

        self.BindingSignal()
        self.SetStyle()






    def InitializeComponent(self):
        self.setWindowTitle('Приложение №2 ver 2')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout_central_widget = QVBoxLayout()
        layout_central_widget.setSpacing(0)
        layout_central_widget.setContentsMargins(15, 0, 15, 10)

        central_widget.setLayout(layout_central_widget)
        self.title_bar = MyCustomTittleBar(self)


        widget_work = QWidget()


        layout_central_widget.addWidget(self.title_bar)
        layout_central_widget.addWidget(widget_work)

        layot_work_widget = QVBoxLayout()
        layot_work_widget.setContentsMargins(15, 0, 15, 0)
        layot_work_widget.setSpacing(1)

        widget_work.setLayout(layot_work_widget)
        grid = QGridLayout()




        self.label_title = QLabel('Заглавный лейбл')
        self.label_type_profile = QLabel('Тип профиля')
        self.label_type_profile.setObjectName('label_standard')
        self.label_profile = QLabel('Профиль')
        self.label_profile.setObjectName('label_standard')
        self.label_steel = QLabel('Сталь')
        self.label_steel.setObjectName('label_standard')

        self.combobox_type_profile = QComboBox()
        self.combobox_profile = QComboBox()
        self.combobox_grade_steel = QComboBox()
        self.button = QPushButton('Типо будет экспорт в WORD')

        #self.output = QTextEdit()

        self.widgetInfo = QWidget()

        self.layot_widgetInfo = QVBoxLayout()
        self.layot_widgetInfo.setSpacing(0)

        self.widgetInfo.setLayout(self.layot_widgetInfo)

        grid.addWidget(self.label_type_profile, 0, 0)
        grid.addWidget(self.label_profile, 0, 1)
        grid.addWidget(self.label_steel, 0, 2)
        grid.addWidget(self.combobox_type_profile, 1, 0)
        grid.addWidget(self.combobox_profile, 1, 1)
        grid.addWidget(self.combobox_grade_steel, 1, 2)



        layot_work_widget.addWidget(self.label_title)
        layot_work_widget.addLayout(grid)
        #layot_work_widget.addWidget(self.output)
        layot_work_widget.addWidget(self.widgetInfo)
        layot_work_widget.addWidget(self.button)







    def SetValuesDefault(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.combobox_type_profile.addItems(['Труба', 'Двутавр'])
        self.set_values_cb_profile(self.combobox_type_profile.currentText())
        self.set_values_cb_grade_steel(self.combobox_type_profile.currentText())

        self.get_output()



    def SetStyle(self):
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint)

        self.setObjectName('Main')

        #self.setStyleSheet('background-color: green')


        self.label_title.setStyleSheet('font-size:25pt; '
                                       'font-family:GOST 2.304 type A; '
                                       'color: white;'
                                       'border: 5px solid gold;'
                                       'background-color: black')
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        self.setMinimumWidth(400)
        self.setMinimumHeight(600)

    def BindingSignal(self):
        self.button.clicked.connect(self.the_button_click)
        self.combobox_type_profile.currentTextChanged.connect(self.the_cb_type_change)
        self.combobox_profile.currentTextChanged.connect(self.the_cb_profile_change)
        self.combobox_grade_steel.currentTextChanged.connect(self.the_cb_grade_steel)

    def the_button_click(self):
        print('click')
        print(self.combobox_type_profile.currentIndex())
        print(self.combobox_type_profile.currentText())
        print()

    def the_cb_type_change(self):

        self.set_values_cb_profile(self.combobox_type_profile.currentText())
        self.set_values_cb_grade_steel(self.combobox_type_profile.currentText())

    def the_cb_profile_change(self):
        self.get_output()


    def the_cb_grade_steel(self):
        self.get_output()

    def set_values_cb_profile(self, type_profile):
        self.combobox_profile.clear()

        if type_profile == "Двутавр":
            self.cursor.execute('SELECT section_name FROM Data_Ibeam_profile ORDER BY id ASC')
            profile_list = []
            profiles = self.cursor.fetchall()
            for profile in profiles:
                profile_list.append(profile[0])
            self.combobox_profile.addItems(profile_list)

        elif type_profile == "Труба":
            self.cursor.execute('SELECT section_name FROM Data_Tube_profile')
            profile_list = []
            profiles = self.cursor.fetchall()
            for profile in profiles:
                profile_list.append(profile[0])
            self.combobox_profile.addItems(profile_list)


    def set_values_cb_grade_steel(self, type_profile):
        self.combobox_grade_steel.clear()
        if type_profile == "Двутавр":
            self.cursor.execute('SELECT steel_name FROM Data_Ibeam_material GROUP BY steel_name')
            material_list = []
            profiles = self.cursor.fetchall()
            for profile in profiles:
                material_list.append(profile[0])
            self.combobox_grade_steel.addItems(material_list)


        elif type_profile == "Труба":
            self.cursor.execute('SELECT steel_name FROM Data_Tube_material GROUP BY steel_name')
            material_list = []
            profiles = self.cursor.fetchall()
            for profile in profiles:
                material_list.append(profile[0])
            self.combobox_grade_steel.addItems(material_list)

    def get_output(self):
        type_profile = self.combobox_type_profile.currentText()
        profile = self.combobox_profile.currentText()
        grade_steel = self.combobox_grade_steel.currentText()
        text = ''

        if type_profile == 'Двутавр':
            self.cursor.execute(
                f'SELECT section_name, height, width, web_thickness, flange_thickness, square, moment_of_inertia_x, '
                f'moment_of_inertia_y FROM Data_Ibeam_profile WHERE section_name = "{profile}"')

            query = self.cursor.fetchone()
            if query is not None:
                height = query[1]
                width = query[2]
                web_thickness = query[3]
                flange_thickness = query[4]
                square = query[5]
                moment_of_inertia_x = query[6]
                moment_of_inertia_y = query[7]
                self.cursor.execute(
                    f'SELECT Ry FROM Data_Ibeam_material '
                    f'WHERE steel_name = "{grade_steel}" AND '
                    f'thickness_min <={flange_thickness} '
                    f'AND thickness_max > {flange_thickness}')
                query = self.cursor.fetchone()
                if query is not None:
                    r_y = query[0]
                    reportList = [f'Тип профиля: {type_profile}', f'Профиль: {profile}', f'Сталь: {grade_steel}',
                                  f'Высота: {height} мм', f'Ширина: {width}',
                                  f'Толщина стенки: $t_{'w'} = {web_thickness} мм$',
                                  f'Толщина полки: $t_{'f'} = {flange_thickness} мм$',
                                  f'Площадь: $A={square}см^{2}$',
                                  f'Момент инерции x-x: $I_{'x'}={moment_of_inertia_x}см^{4}$',
                                  f'Момент инерции y-y: $I_{'y'}={moment_of_inertia_y}см^{4}$',
                                  f'Расчетное сопротивление стали: $R_{'y'}={r_y}Н/мм^{2}$']
                    self.setFormulaList(reportList)

        elif type_profile == 'Труба':
            self.cursor.execute(f'SELECT section_name, height, width, thickness, square, moment_of_inertia_x, '
               f'moment_of_inertia_y FROM Data_Tube_profile WHERE section_name = "{profile}"')
            query = self.cursor.fetchone()
            if query is not None:
                height = query[1]
                width = query[2]
                thickness = query[3]
                square = query[4]
                moment_of_inertia_x = query[5]
                moment_of_inertia_y = query[6]

                self.cursor.execute(
                    f'SELECT Ry FROM Data_Tube_material '
                    f'WHERE steel_name = "{grade_steel}" AND '
                    f'thickness_min <={thickness} '
                    f'AND thickness_max > {thickness}')
                query = self.cursor.fetchone()
                if query is not None:
                    r_y = query[0]

                    reportList = [f'Тип профиля: {type_profile}',
                                  f'Профиль: {profile}',
                                  f'Сталь: {grade_steel}',
                                  f'Высота: {height} мм',
                                  f'Ширина: {width} мм',
                                  f'Толщина : $t_{'w'} = {thickness} мм$',
                                  f'Площадь: $A={square}см^{2}$',
                                  f'Момент инерции x-x: $I_{'x'}={moment_of_inertia_x}см^{4}$',
                                  f'Момент инерции y-y: $I_{'y'}={moment_of_inertia_y}см^{4}$',
                                  f'Расчетное сопротивление стали: $R_{'y'}={r_y}Н/мм^{2}$']
                    self.setFormulaList(reportList)





        #self.output.setText(text)



    def setFormulaList(self, formulaList):
        self.clear_layout_widgetInfo()

        for text in formulaList:
            pixmap = mathTex_to_QPixmap(text, 15)
            label_row_info = QLabel()
            label_row_info.setObjectName('label_row')
            label_row_info.setStyleSheet('background-color:red;'
                                 'font: bold;'
                                 'border: none;'
                                 'padding-left:10px;'
                                 'padding-right:100px;'
                                 'padding-top:1px')
            label_row_info.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
            label_row_info.setPixmap(pixmap)
            self.layot_widgetInfo.addWidget(label_row_info)
        label_end_row = QLabel()
        label_end_row.setStyleSheet('background-color:red;'
                             'border: none;'
                             'font-size:15pt;'
                             'padding-left:10px;'
                             'padding-top:1px;'
                             'font-family:GOST 2.304 type A')
        label_end_row.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layot_widgetInfo.addWidget(label_end_row)
        self.layot_widgetInfo.count()

    def clear_layout_widgetInfo(self):
        while self.layot_widgetInfo.count() > 0:
            widgetToRemove = self.layot_widgetInfo.takeAt(0).widget()
            widgetToRemove.deleteLater()




    def closeEvent(self, a0):
        self.connection.close()


StyleSheet = """

QMainWindow {
    background-color: green;
}
QLabel#label_standard {
    font-size:15pt;
    font-family:GOST 2.304 type A;
    border: 2px solid black;
    border-radius: 10px;
    background-color: red;
    padding-left:20px;     
}
QPushButton {
    color: white;
    background-color: black;
    border: 2px solid black;
    border-radius: 10px;
    font-size:15pt;
    font-family:GOST 2.304 type A;
}
QPushButton:hover {
    color: black;
    background-color: gold;
    font-weight:bold;
    
    
}
QPushButton:pressed {
    color: gold;
    background-color: red;
    
}


QComboBox {
    background-color: red;
    border: 2px solid black;
    border-radius: 10px;
    padding: 1px 18px 1px 3px;
    min-width: 6em;
    font-size:15pt;
    font-family:GOST 2.304 type A;
}
QComboBox QAbstractItemView {
    border: 2px solid blue;
    selection-background-color: red;
    background-color: yellow;
    border-radius: 10px;
}

"""

app = QApplication(sys.argv)
app.setStyleSheet(StyleSheet)
window = Mainwindow()
window.show()

app.exec()