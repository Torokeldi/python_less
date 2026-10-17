users = {
    "admin": "1243",
    "user": "qwerty"
}

login = input("Введите логин: ")

try:
    print(f"Пароль: {users[login]}")
except KeyError:
    print("такого логина нет")



age = input("Введите ваш возраст: ")

if age.isdigit():
    print("Доступ разрешен.")
elif age and age[0] == "-" and age[1:].isdigit():
    print("отрицательное число")
else:
    print("не является числом")




try:
    password = input("Введите пароль: ")

    v = 1 / len(password)

    print(f"Длина пароля: {len(password)}")

except ZeroDivisionError:
    print("пользователь нажал Enter")



nomer1 = int(input("первое число: "))
nomer2 = int(input("второе число: "))
operation = input("операция:")

try:
    if operation == "+":
        print(nomer1 + nomer2)
    elif operation == "-":
        print(nomer1 - nomer2)
    elif operation == "*":
        print(nomer1 * nomer2)
    elif operation == "/":
        print(nomer1 / nomer2)
    elif operation == "^":
        print(nomer1 ** nomer2)
    elif operation == "%":
        print(nomer1 % nomer2)
    elif operation == ">":
        print(nomer1 > nomer2)
    elif operation == "<":
        print(nomer1 < nomer2)
    elif operation == ">=":
        print(nomer1 >= nomer2)
    elif operation == "<=":
        print(nomer1 <= nomer2)
    elif operation == "==":
        print(nomer1 == nomer2)
    elif operation == "!=":
        print(nomer1 != nomer2)