import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Выбираем первого пользователя
cursor.execute('SELECT * FROM Users')
first_user = cursor.fetchone()
print(first_user)

# Выбираем первых 5 пользователей
cursor.execute('SELECT * FROM Users')
first_five_users = cursor.fetchmany(5)
print(first_five_users)

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
all_users = cursor.fetchall()
print(all_users)

# Закрываем соединение
connection.close()