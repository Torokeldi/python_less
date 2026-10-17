#TUPLES

tuple1 = (9, 6 ,5)
print(tuple1[::2])

tuple2 = (9, 6, 5, 4, 8, 7)
tuple3 = ("John", "Simon", "Clarke", "Justin")
print(tuple2 + tuple3)

tuple4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n = tuple4[::-2]
p = n[::-1]
print(p)

nums = (1, 2, 3, 4, 5)
nn = list(nums)
nn[2] = 99
nums = tuple(nn)
print(nums)

numbers = (66, 99, 40, 70, 34, 56, 44, 87)
summ = min(numbers), max(numbers)
print(summ)

s = "hello world"
l = tuple(s).count("o")
print(l)



#PASSWORD

user = input("введите пароль: ")

ll = list(user)

num = False
txt = False
long = False
sym = False

for i in ll:
    if i.isdigit():
        num = True
    if i.isalpha():
        txt = True
    if i in "`~!@#$<%^&*(>)_+{\\/?}|:;][.,-=\"\'":
        sym = True
    if len(ll) >= 8:
        long = True

q = [
    "нет букв",
    "нет цифр",
    "длина должна быть не менее 8",
    "нет специальных символов",
    "надёжный пароль"
]

if txt == False:
    print(q[0])

if num == False:
    print(q[1])

if long == False:
    print(q[2])

if sym == False:
    print(q[3])

if txt and num and long and sym:
    print(q[4])


# DICTIONARY

movie = {
    "название": "Человек-паук",
    "год выпуска": 2002,
    "режиссер": "Сэм Рэйми",
    "главные актеры": [ "Тоби Магуайр", "Уиллем Дефо", "Кирстен Данст", "Джеймс Франко", "Клифф Робертсон", "Розмари Харрис", "Дж.К. Симмонс", "Джо Манганьелло", "Майкл Пападжон", "Билл Нанн"
]
}

print(movie)

dict = {
    "apple": "яблоко",
    "book": "книга",
    "cat": "кот",
    "dog": "собака",
    "sun": "солнце"
}

word = input("Введи слово на английском: ").strip().lower()

if word in dict:
    print(f"Перевод слова '{word}': {dict[word]}")
else:
    print("К сожалению, этого слова нет в словаре.")

city = {
    "название": "Сеул",
    "страна": "Юж. Корея",
    "население":  9602826,
    "достопримечательности": ["Дворец Кёнбоккун", "Ворота Намдэмун", "Деловой район Каннам"]
}

print(city)


