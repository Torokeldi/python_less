#1
Musk = '3000000000000'
print(Musk.count('0'))

#2
a = 25
b = 75
c = 10
d = 95
e = (a + b + c + d) / 4
print(e)

#3
s = 'Kyrgyz'
t = 'Republic'
r = s.upper(), t.lower()
print(r)

#4
x = 'Google создаст специальную команду для поиска багов особо важных приложениях'
y = len(x.split())
print(y)

#5
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
movie = input("Введите ваш любимый фильм: ")

st = "Привет,", name + "! Тебе", age, "лет. Фильм", movie, "очень интересный! Ты выбрал классный фильм."
print(st)

#6
qw = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
res = qw.replace('е','3' )

print(res)

#7
n = input("Введите строку: ")
m = n.lower()

print(m)

#8
pas = input('Enter password: ')
rrr = len(pas)
ccc = pas.lower(), pas.upper()
print(rrr, ccc)

#9
login = input('enter your login: ')
print(login.strip())

#10
name, surname = input().split()
txt = name[0] + '.' + surname[0]
print(txt)
