# from abc import ABC, abstractmethod
#
# class CoffeeMachine(ABC):
#     @abstractmethod
#     def make_coffee(self):
#         pass
#
# class LatteMachine(CoffeeMachine):
#     def make_coffee(self):
#         print("Latte даяр ")
#
# class EspressoMachine(CoffeeMachine):
#     def make_coffee(self):
#         print("Espresso даяр ")
#
# latte = LatteMachine()
# latte.make_coffee()
#
# espresso = EspressoMachine()
# espresso.make_coffee()
#
#
#
# class GameCharacter(ABC):
#     @abstractmethod
#     def attack(self):
#         pass
#
# class Warrior(GameCharacter):
#     def attack(self):
#         print("Кылыч менен чабуул жасады")
#
# class Archer(GameCharacter):
#     def attack(self):
#         print("Жаа менен атты")
#
# warrior = Warrior()
# warrior.attack()
#
# archer = Archer()
# archer.attack()
#
#
#
#
# class Notification(ABC):
#     @abstractmethod
#     def send(self):
#         pass
#
# class SMS(Notification):
#     def send(self):
#         print("SMS кетти")
#
# class Email(Notification):
#     def send(self):
#         print("Email кетти")
#
# sms_notif = SMS()
# sms_notif.send()
#
# email_notif = Email()
# email_notif.send()
