
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('SELECT section_name FROM Data_Ibeam_profile WHERE reduced_assortment = 1')

profile_list = []

profiles = cursor.fetchall()
for profile in profiles:
    print(profile)
    profile_list.append(profile[0])


print(profile_list)

print()

profile = '10Б1'
cursor.execute(f'SELECT section_name, height, width, web_thickness, flange_thickness, square, moment_of_inertia_x, '
               f'moment_of_inertia_y FROM Data_Ibeam_profile WHERE section_name = "{profile}"')

query = cursor.fetchone()
height = str(query[1])
print(height)
print(query)
print()

cursor.execute('SELECT section_name FROM Data_Ibeam_profile ORDER BY id ASC')
query = cursor.fetchall()
listProfiles = [prof[0] for prof in query]

print(query)
print()
print(listProfiles)




