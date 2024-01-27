import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# Преобразуем результаты в список словарей
users_list = []
for user in users:
  user_dict = {
    'id': user[0],
    'username': user[1],
    'email': user[2],
    'age': user[3]
  }
users_list.append(user_dict)

# Выводим результаты
for user in users_list:
  print(user)

# Закрываем соединение
connection.close()