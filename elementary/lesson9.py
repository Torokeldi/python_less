n1 = [2, 4, 6, 8]
for x in n1:
    if x % 2 == 0:
        print(x)

n2 = [10, 3, 25, 7, 18]
for x in n2:
    if x > 10:
        print(x)

n3 = [1, 2, 3, 4]
res3 = []
for x in n3:
    res3.insert(0, x)
print(res3)

t = "python"
for c in t:
    print(c)

n5 = [5, 10, 15]
i = 0
for x in n5:
    print(f"{i} -> {x}")
    i += 1

n6 = [1, 4, 7, 2, 9, 6]
k = 0
for x in n6:
    if x > 5:
        k += 1
print(k)

n7 = [3, 5, 7, 9]
res7 = []
for x in n7:
    res7.append(x * 2)
print(res7)

ik = [
    'брюки', 'очки', 'плавки', 'ноутбук', 'зарядниик',
    'загар крем', 'футболка', 'кроссы', 'брюки', 'очки',
    'плавки', 'загар крем', 'футболка', 'кроссы', 'брюки', 'зарядниик'
]

a = []
b = []
qwerty = [a, b]

for i in ik:
    f = False

    if i in qwerty[0]:
        f = True
        if f:
            qwerty[1].append(i)
        else:
            qwerty[0].append(i)

print("Взял с собой", a)
print("Оставил дома", b)
