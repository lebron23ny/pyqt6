import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Обновляем возраст пользователя "newuser"
cursor.execute('UPDATE Users SET age = ? WHERE username = ?',
               (29, 'newuser'))


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
