import sqlite3
#Сортировка по убвывания DESC, по возрастанию ASC
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Выбираем и сортируем пользователей по возрасту по убыванию
cursor.execute('SELECT username, age FROM Users ORDER BY age ASC')
results = cursor.fetchall()

for row in results:
  print(row)


# Закрываем соединение
connection.close()