#1
a = int(input('возраст: '))
if a >= 18:
    print('заходить')
elif a < 18:
    print('уходить')

#2
b = int(input('номер: '))
if b > 0:
    print('положительный')
elif b < 0:
    print('отрицательный')
else:
    print('равно')

#3
c = int(input('номер: '))
if c % 2 == 0:
    print('четный')
else:
    print('нечетный')

#4
d = input('пароль: ')
if d == 'admin123':
    print('доступ открыт')
else:
    print('неверный')

#5
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))

if first > second:
    print("Первое больше")
elif second > first:
    print("Второе больше")
else:
    print("Они равны")

#6
e = int(input("Введите оценку от 1 до 5: "))

if e == 5:
    print("Отлично")
elif e == 4:
    print("Хорошо")
elif e == 3:
    print("Удовлетворительно")
elif e == 2:
    print("Плохо")
else:
    print("Очень плохо")

#7
a1 = 10
b1 = 5

if a1 > 0 and b1 > 0:
    print("Оба числа положительные")

if a1 > b1:
    print(a1 + 2)
else:
    print(b1 + 2)

#8
f = int(input("Введите сумму: "))

if f >= 500 and f % 500 == 0:
    print("Сумма доступна для снятия.")
else:
    print("Невозможно снять сумму.")

#9
g = int(input("Вес арбуза: "))

if g % 2 == 0 and g > 2:
    print("да")
else:
    print("нет")

#10
h = int(input("первая сумма: "))
i = int(input("вторая сумма: "))
j = int(input("третий сумма: "))
sum = h + i + j

if sum > 10000:
    k = (sum * 10) / 100
    sum = sum - k

print("Итого: ", sum)

#11
l = int(input("Сколько счета на кармане? "))

m = 36000

if l >= m:
    l -= m
    print("Курс успешно приобретён.")

print("Хорошего дня!")

#12
n = int(input("Введите сумму: "))

if n % 500 == 0 and n > 0:
    print("Сумма доступна для снятия.")
else:
    print("Такую сумму снять невозможно.")
