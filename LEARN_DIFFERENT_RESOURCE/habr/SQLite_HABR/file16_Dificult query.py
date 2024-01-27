import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Находим пользователей с наибольшим возрастом
cursor.execute('''
SELECT username, age
FROM Users
WHERE age = (SELECT MIN(age) FROM Users)
''')
oldest_users = cursor.fetchall()

# Выводим результаты
for user in oldest_users:
    print(user)

# Закрываем соединение
connection.close()