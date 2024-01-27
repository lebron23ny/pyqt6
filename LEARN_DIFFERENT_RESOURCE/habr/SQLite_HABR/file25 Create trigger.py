import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Создаем триггер для обновления времени создания при вставке новой записи
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_created_at
AFTER INSERT ON Users
BEGIN
UPDATE Users SET created_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()