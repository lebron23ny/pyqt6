import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Удаляем пользователя "newuser"
cursor.execute('DELETE FROM Users WHERE username = ?',
               ('newuser',))


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
