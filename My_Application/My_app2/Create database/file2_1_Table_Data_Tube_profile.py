import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data_Tube_profile (
    section_name TEXT PRIMARY KEY,
    reduced_assortment INTEGER NOT NULL,
    thickness REAL NOT NULL,    
    height REAL NOT NULL,
    width REAL NOT NULL,
    square REAL NOT NULL,    
    moment_of_inertia_x REAL NOT NULL,
    moment_of_resistance_x REAL NOT NULL,
    radius_inertia_x REAL NOT NULL,
    moment_of_inertia_y REAL NOT NULL,
    moment_of_resistance_y REAL NOT NULL,
    radius_inertia_y REAL NOT NULL,
    linear_weight NOT NULL,
    radius_of_curvature NOT NULL,
    perimeter NOT NULL)
    '''
               )

cursor.execute('CREATE INDEX idn_section_name_tube ON Data_Tube_profile (section_name)')
cursor.execute('CREATE INDEX idn_reduced_assortment_tube ON Data_Tube_profile (reduced_assortment)')
# Сохраняем изменения и закрываем соединение
connection.commit()


connection.close()