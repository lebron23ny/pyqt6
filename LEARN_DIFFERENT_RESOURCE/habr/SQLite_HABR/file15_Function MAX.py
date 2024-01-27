import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Нахождение минимального возраста
cursor.execute('SELECT MIN(age) FROM Users')
min_age = cursor.fetchone()[0]

print('Минимальный возраст среди пользователей:', min_age)
connection.close()