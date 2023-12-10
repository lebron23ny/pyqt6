import openpyxl
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

wb = openpyxl.load_workbook('Data.xlsx', data_only=True)
sheet_tube = wb['Профили_ГСП']
max_row = sheet_tube.max_row



print()

for i in range(3, max_row + 1):
    section = sheet_tube['A' + str(i)].value
    if sheet_tube['B' + str(i)].value == "нет":
        reduced_assortment = 0
    else:
        reduced_assortment = 1

    thickness = float(sheet_tube['C' + str(i)].value)
    height = float(sheet_tube['D' + str(i)].value)
    width = float(sheet_tube['E' + str(i)].value)
    square = float(sheet_tube['F' + str(i)].value)
    moment_of_inertia_x = float(sheet_tube['G' + str(i)].value)
    moment_of_resistance_x = float(sheet_tube['H' + str(i)].value)
    radius_inertia_x = float(sheet_tube['I' + str(i)].value)
    moment_of_inertia_y = float(sheet_tube['J' + str(i)].value)
    moment_of_resistance_y = float(sheet_tube['K' + str(i)].value)
    radius_inertia_y = float(sheet_tube['L' + str(i)].value)
    linear_weight = float(sheet_tube['M' + str(i)].value)
    radius_of_curvature = float(sheet_tube['N' + str(i)].value)
    perimeter = float(sheet_tube['O' + str(i)].value)

    cursor.execute('INSERT INTO Data_Tube_profile (section_name, reduced_assortment, thickness, height, width,'
                   'square, '
                   'moment_of_inertia_x, moment_of_resistance_x, radius_inertia_x, '
                   'moment_of_inertia_y, moment_of_resistance_y, radius_inertia_y, '
                   'linear_weight, radius_of_curvature, perimeter) '
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (section, reduced_assortment, thickness, height, width, square,
                    moment_of_inertia_x, moment_of_resistance_x, radius_inertia_x,
                    moment_of_inertia_y, moment_of_resistance_y, radius_inertia_y,
                    linear_weight, radius_of_curvature, perimeter))

connection.commit()
connection.close()
print('ВСЕ!')
