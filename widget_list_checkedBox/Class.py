

class Person:
    def __init__(self, name, age, gender):
        self.__age = age
        self.__name = name
        self.gender = gender


    def __str__(self):
        return f'Имя: {self.__name}, возраст: {self.__age}'





p1 = Person('Tom', 25, 'male')
p2 = Person('Helga', 18, 'female')


d = p1.gender
print(d)