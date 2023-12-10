import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data_Tube_material (
    id INTEGER PRIMARY KEY,
    steel_name TEXT NOT NULL,
    thickness_min REAL NOT NULL,
    thickness_max REAL NOT NULL,
    Ryn REAL NOT NULL,
    Run REAL NOT NULL,
    Ry REAL NOT NULL,
    Ru REAL NOT NULL,
    Rbp_A REAL NOT NULL,
    Rbp_B REAL NOT NULL)
    '''
               )

cursor.execute('CREATE INDEX idn_steel_name_Tube ON Data_Tube_material (steel_name)')

# Сохраняем изменения и закрываем соединение
connection.commit()


connection.close()