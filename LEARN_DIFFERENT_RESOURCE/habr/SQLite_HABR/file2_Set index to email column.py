import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем индекс для столбца "email"
cursor.execute('CREATE INDEX idx_email ON Users (email)')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

