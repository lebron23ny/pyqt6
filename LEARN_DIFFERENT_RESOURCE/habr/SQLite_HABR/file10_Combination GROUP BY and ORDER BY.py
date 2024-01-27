import sqlite3
#Сортировка по убвывания DESC, по возрастанию ASC
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Выбираем и сортируем пользователей по возрасту по убыванию
cursor.execute('''
SELECT username, age, AVG(age)
FROM Users
GROUP BY age
HAVING AVG(age) > ?
ORDER BY age DESC
''', (18,))
results = cursor.fetchall()

for row in results:
  print(row)

connection.close()