import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Вычисление суммы возрастов пользователей
cursor.execute('SELECT SUM(age) FROM Users')


total_age = cursor.fetchone()[0]

print('Общая сумма возрастов пользователей:', total_age)
connection.close()