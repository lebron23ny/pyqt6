import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем индекс для столбца "username"
cursor.execute('CREATE INDEX idx_username ON Users (username)')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
