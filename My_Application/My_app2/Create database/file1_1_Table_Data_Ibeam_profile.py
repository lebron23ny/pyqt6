import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data_Ibeam_profile (
    id INTEGER PRIMARY KEY,
    section_name TEXT NOT NULL,
    reduced_assortment INTEGER NOT NULL,
    height REAL NOT NULL,
    width REAL NOT NULL,
    web_thickness REAL NOT NULL,
    flange_thickness REAL NOT NULL,
    web_height REAL NOT NULL,
    flange_overhang REAL NOT NULL,
    radius REAL NOT NULL,
    square REAL NOT NULL,
    moment_of_inertia_x REAL NOT NULL,
    moment_of_resistance_x REAL NOT NULL,
    static_moment_half_x REAL NOT NULL,
    radius_inertia_x REAL NOT NULL,
    moment_of_inertia_y REAL NOT NULL,
    moment_of_resistance_y REAL NOT NULL,
    static_moment_half_y REAL NOT NULL,
    radius_inertia_y REAL NOT NULL)
    '''
               )

cursor.execute('CREATE INDEX idn_section_name ON Data_Ibeam_profile (section_name)')
cursor.execute('CREATE INDEX idn_reduced_assortment ON Data_Ibeam_profile (reduced_assortment)')
# Сохраняем изменения и закрываем соединение
connection.commit()


connection.close()