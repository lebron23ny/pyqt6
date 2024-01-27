import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Вычисление среднего возраста пользователей
cursor.execute('SELECT AVG(age) FROM Users')
average_age = cursor.fetchone()[0]

print('Средний возраст пользователей:', average_age)
connection.close()