class Student:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def __str__(self):
        return f"Студент: имя - {self.name}, возраст - {self.age}"
print(Student("Bakyt", 18))

class Car:
    def __init__(self, brand, color):
        self.brand, self.color = brand, color
    def __str__(self):
        return f"Машина: марка - {self.brand}, цвет - {self.color}"
print(Car("Fiat", "green"))

class Book:
    def __init__(self, title, author):
        self.title, self.author = title, author
    def __str__(self):
        return f"Книга: название - '{self.title}', автор - {self.author}"
print(Book("Руслан и Людмила", "А. Пушкин"))

class Phone:
    def __init__(self, model, price):
        self.model, self.price = model, price
    def __str__(self):
        return f"Телефон: модель - {self.model}, цена - {self.price} сом"

print(Phone("iPhone 15", 80000))

class Animal:
    def __init__(self, name, sound):
        self.name, self.sound = name, sound
    def __str__(self):
        return f"Животное: название - {self.name}, звук - {self.sound}"

print(Animal("Собака", "гаф-гаф"))
