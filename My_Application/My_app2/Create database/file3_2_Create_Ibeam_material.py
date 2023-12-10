import openpyxl
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

wb = openpyxl.load_workbook('Data.xlsx', data_only=True)
sheet_Ibeam_material = wb['Сталь Двутавр']
max_row = sheet_Ibeam_material.max_row
print(max_row)

for i in range(3, max_row + 1):
    steel_name = sheet_Ibeam_material['A' + str(i)].value
    thickness_min = sheet_Ibeam_material['B' + str(i)].value

    thickness_max = float(sheet_Ibeam_material['C' + str(i)].value)
    Ryn = float(sheet_Ibeam_material['D' + str(i)].value)
    Run = float(sheet_Ibeam_material['E' + str(i)].value)
    Ry = float(sheet_Ibeam_material['F' + str(i)].value)
    Ru = float(sheet_Ibeam_material['G' + str(i)].value)
    Rbp_A = float(sheet_Ibeam_material['H' + str(i)].value)
    Rbp_B = float(sheet_Ibeam_material['I' + str(i)].value)

    cursor.execute('INSERT INTO Data_Ibeam_material (steel_name, thickness_min, thickness_max, Ryn, Run,'
                   'Ry, Ru, Rbp_A, Rbp_B) '
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (steel_name, thickness_min, thickness_max, Ryn, Run, Ry,
                    Ru, Rbp_A, Rbp_B))

connection.commit()
connection.close()
print('ВСЕ!')
