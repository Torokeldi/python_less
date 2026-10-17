# 2 class Notification:
#     def send(self, message):
#         pass
#
# class EmailNotification(Notification):
#     def send(self, message):
#         print(f"Email жөнөтүлдү: {message}")
#
# class SMSNotification(Notification):
#     def send(self, message):
#         print(f"SMS жөнөтүлдү: {message}")
#
# class TelegramNotification(Notification):
#     def send(self, message):
#         print(f"Telegram жөнөтүлдү: {message}")
#
# notifications = [EmailNotification(), SMSNotification(), TelegramNotification()]
# for notif in notifications:
#     notif.send("Салам!")
#
#
#
#
# class Character:
#     def attack(self):
#         pass
#
# class Warrior(Character):
#     def attack(self):
#         print("Warrior - кылыч менен чабат")
#
# class Archer(Character):
#     def attack(self):
#         print("Archer - жаа менен атат")
#
# class Mage(Character):
#     def attack(self):
#         print("Mage - сыйкыр колдонуп чабат")
#
# characters = [Warrior(), Archer(), Mage()]
#
# for character in characters:
#     character.attack()
#
#
#
#
# class Player:
#     def play(self):
#         pass
#
# class Spotify(Player):
#     def play(self):
#         print("Spotify музыка ойнотту")
#
# class YouTube(Player):
#     def play(self):
#         print("YouTube видео ойнотту")
#
# class Radio(Player):
#     def play(self):
#         print("Радио музыка ойнотту")
#
# players = [Spotify(), YouTube(), Radio()]
#
# for player in players:
#     player.play()
#
#
#
#
#
# class Delivery:
#     def deliver(self):
#         pass
#
# class Courier(Delivery):
#     def deliver(self):
#         print("Курьер товарды жөө жеткирди")
#
# class Post(Delivery):
#     def deliver(self):
#         print("Почта аркылуу товар жөнөтүлдү")
#
# class Taxi(Delivery):
#     def deliver(self):
#         print("Такси менен товар жеткирилди")
#
# deliveries = [Courier(), Post(), Taxi()]
#
# for service in deliveries:
#     service.deliver()
#
#
#
#
#
#
# class SocialMedia:
#     def post(self, content):
#         pass
#
# class Instagram(SocialMedia):
#     def post(self, content):
#         print(f"Instagram: История киргизилди -> {content}")
#
# class YouTube(SocialMedia):
#     def post(self, content):
#         print(f"YouTube: Видео киргизилди -> {content}")
#
# class TikTok(SocialMedia):
#     def post(self, content):
#         print(f"TikTok: Кыска видео киргизилди -> {content}")
#
# social_networks = [Instagram(), YouTube(), TikTok()]
#
# for network in social_networks:
#     network.post("Менин постум")
