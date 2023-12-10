import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('SELECT section_name FROM Reduced_assortment_Ibeam')

profiles = cursor.fetchall()
print(f'Всего профилей: {len(profiles)}')
# for profile in profiles:
#     print(profile)

cursor.execute('UPDATE Data_Ibeam_profile SET reduced_assortment = ? WHERE section_name = ?',
               (1, '16Б1'))


cursor.execute('SELECT section_name FROM Reduced_assortment_Ibeam')

profiles = cursor.fetchall()
print(f'Всего профилей: {len(profiles)}')

connection.commit()
connection.close()
