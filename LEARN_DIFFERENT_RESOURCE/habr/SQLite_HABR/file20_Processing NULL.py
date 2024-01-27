import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Выбираем пользователей с неизвестным возрастом
cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unknown_age_users = cursor.fetchall()

# Выводим результаты
for user in unknown_age_users:
  print(user)

# Закрываем соединение
connection.close()
