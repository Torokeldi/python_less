class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


personn = Person("Asan", 26)

print("Аты:", personn.name)
print("Жашы:", personn.age)





class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Баланс толтурулду: +{amount}")
        else:
            print("Ката: Сумма нөлдөн чоң болушу керек!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)

print("Учурдагы баланс:", account.get_balance())




class Animal:
    def sound(self):
        print("Жаныбар үн чыгарат")

class Dog(Animal):
    pass

myDog = Dog()

myDog.sound()





class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

student1 = Student("Асан", 11)

print(f"Аты: {student1.name}, Классы: {student1.grade}")





class Cat:
    def sound(self):
        return "Мяу"

class Dog:
    def sound(self):
        return "Гав"

animals = [Cat(), Dog()]

for animal in animals:
    print(animal.sound())






class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        if password == self.__password:
            print("Туура")
        else:
            print("Ката (Неверно)")

user1 = User("secret123")
user1.check_password("secret123")




class Vehicle:
    def move(self):
        return "Транспорт журуп жатат"

class Car(Vehicle):
    pass

my_car = Car()
print(my_car.move())







class Bird:
    def move(self):
        return "чымчык учат"
class Fish:
    def move(self):
        return "балык сүзөт"
class Dog:
    def move(self):
        return "ит чуркайт"

bird = Bird()
fish = Fish()
dog = Dog()

animals = [bird, fish, dog]

for animal in animals:
    print(animal.move())
