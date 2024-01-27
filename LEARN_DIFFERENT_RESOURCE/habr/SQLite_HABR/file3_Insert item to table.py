import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Добавляем нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
               ('Bob', 'newuser@example.com', 28))
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
               ('John', 'newuser@example.com', None))


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
