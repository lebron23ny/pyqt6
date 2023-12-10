
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()



print()

profile = '100x50x4'
cursor.execute(f'SELECT section_name, height, width, thickness, square, moment_of_inertia_x, '
               f'moment_of_inertia_y FROM Data_Tube_profile WHERE section_name = "{profile}"')

query = cursor.fetchone()

print(query)




