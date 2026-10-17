#1
menu = [
    'lagman 150 som',
    'plov 300 som',
    'borsh 500 som',
    'manty 400 som'
]

menu.append('beshbarmak 280 som')
menu.remove('borsh 500 som')
menu.remove('manty 400 som')
menu.append('manty 310 som')
print(menu)

#2
a = ['white', 'green', 'black', 'blue', 'red']
b = ['dog', 'cow', 'goat', 'cat']
a.extend(b)
print(a)

#3
names = [
    'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy',
    'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',
    'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon'
]
count = names.count('Jack')
print(count)

#4
names = [
    'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy',
    'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',
    'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon'
]

if "Oskar" in names:
    names.remove("Oskar")
    print("Oskar успешно удален.")
else:
    print("Имени Oskar нет в списке.")

#5

info = []

info.append(input('ваше имя: '))
info.append(int(input('ваш возраст: ')))
info.append(input('ваш любимый язык программирование: '))

print(info)

#6
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
loop = pythonList.index("loop")
pythonList.pop(loop)
print(pythonList)

#7
numbers = [100, 200, 300, 400, 500, 600]
w = numbers[::-1]
print(w)

#8
text = input("Введите строку: ")
words = text.split()
s = len(words)
print(s)

#9
numbers = [1, 2, 3, 4, 5]

q = sum(numbers) / len(numbers)

print(q)
