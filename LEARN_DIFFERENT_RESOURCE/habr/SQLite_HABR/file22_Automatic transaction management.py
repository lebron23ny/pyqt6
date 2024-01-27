import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

try:
    # Начинаем транзакцию
    cursor.execute('BEGIN')

    # Выполняем операции
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)',
                   ('user1', 'user1@example.com'))
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)',
                   ('user2', 'user2@example.com'))

    # Подтверждаем изменения
    cursor.execute('COMMIT')

except:
    # Отменяем транзакцию в случае ошибки
    cursor.execute('ROLLBACK')

# Закрываем соединение
connection.close()