
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


print('Вывести все стали: ')
cursor.execute('SELECT steel_name FROM Data_Tube_material GROUP BY steel_name')

steel_list = cursor.fetchall()
for steel in steel_list:
    print(steel)

print('Вывести Ryn, Run, Ry, Ru, Rbp_A, Rbp_B')
steel_name = 'С345'
thickness = 10
cursor.execute(f'SELECT Ryn, Run, Ry, Ru, Rbp_A, Rbp_B FROM Data_Tube_material WHERE steel_name = "{steel_name}" AND thickness_min <={thickness} AND thickness_max > {thickness}')
#cursor.execute(f'SELECT steel_name, Ryn, Run, Ry, Ru, Rbp_A, Rbp_B FROM Data_Ibeam_material WHERE thickness_min <={thickness} AND thickness_max > {thickness}')


query = cursor.fetchall()
for item in query:
    print(item)

