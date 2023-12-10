#Создадим представление для двутавровых профилей для сокращенного сортамента
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем представление для профилей из сокращенного сортамента

cursor.execute('CREATE VIEW Reduced_assortment_Tube AS SELECT * FROM Data_Tube_profile WHERE reduced_assortment = 1')

connection.close()