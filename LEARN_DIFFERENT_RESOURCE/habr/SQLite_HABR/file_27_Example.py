import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

# Создаем таблицу Tasks
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasks (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
status TEXT DEFAULT 'Not Started'
)
''')


# Функция для добавления новой задачи
def add_task(title):
    cursor.execute('INSERT INTO Tasks (title) VALUES (?)', (title,))
    connection.commit()


# Функция для обновления статуса задачи
def update_task_status(task_id, status):
    cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
    connection.commit()


# Функция для вывода списка задач
def list_tasks():
    cursor.execute('SELECT * FROM Tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)


# Добавляем задачи
add_task('Подготовить презентацию')
add_task('Закончить отчет')
add_task('Подготовить ужин')

# Обновляем статус задачи
update_task_status(2, 'In Progress')

# Выводим список задач
list_tasks()

# Закрываем соединение
connection.close()
