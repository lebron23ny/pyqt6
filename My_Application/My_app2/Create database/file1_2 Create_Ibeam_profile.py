import openpyxl
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

wb = openpyxl.load_workbook('Data.xlsx')
sheet_I_beam = wb['Профили_Двутавры']
max_row = sheet_I_beam.max_row
for i in range(3, max_row + 1):
    section = sheet_I_beam['A' + str(i)].value
    if sheet_I_beam['B' + str(i)].value == "нет":
        reduced_assortment = 0
    else:
        reduced_assortment = 1

    height = float(sheet_I_beam['C' + str(i)].value)
    width = float(sheet_I_beam['D' + str(i)].value)
    web_thickness = float(sheet_I_beam['E' + str(i)].value)
    flange_thickness = float(sheet_I_beam['F' + str(i)].value)
    web_height = float(sheet_I_beam['G' + str(i)].value)
    flange_overhang = float(sheet_I_beam['H' + str(i)].value)
    radius = float(sheet_I_beam['I' + str(i)].value)
    square = float(sheet_I_beam['J' + str(i)].value)
    moment_of_inertia_x = float(sheet_I_beam['K' + str(i)].value)
    moment_of_resistance_x = float(sheet_I_beam['L' + str(i)].value)
    static_moment_half_x = float(sheet_I_beam['M' + str(i)].value)
    radius_inertia_x = float(sheet_I_beam['N' + str(i)].value)
    moment_of_inertia_y = float(sheet_I_beam['O' + str(i)].value)
    moment_of_resistance_y = float(sheet_I_beam['P' + str(i)].value)
    static_moment_half_y = float(sheet_I_beam['Q' + str(i)].value)
    radius_inertia_y = float(sheet_I_beam['R' + str(i)].value)

    cursor.execute('INSERT INTO Data_Ibeam_profile (section_name, reduced_assortment, height, width, web_thickness, '
                   'flange_thickness, web_height, flange_overhang, radius, square, moment_of_inertia_x, '
                   'moment_of_resistance_x, static_moment_half_x, radius_inertia_x, moment_of_inertia_y, '
                   'moment_of_resistance_y, static_moment_half_y, radius_inertia_y) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, '
                   '?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (section, reduced_assortment, height, width, web_thickness, flange_thickness, web_height,
                    flange_overhang, radius, square, moment_of_inertia_x, moment_of_resistance_x, static_moment_half_x,
                    radius_inertia_x, moment_of_inertia_y, moment_of_resistance_y, static_moment_half_y,
                    radius_inertia_y))





connection.commit()
connection.close()
print('ВСЕ!')

