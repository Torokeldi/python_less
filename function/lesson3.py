#1
def lst(name: str, age: int) -> list:
    return [name, age]
print(lst("Torokeldi", 25))

#2
def check_number(a = int(input("num: ")), b = 0):
    if a > b:
        return (
            print("число положительный"))
    elif a < b:
        return (
            print("число отрицательный"))
check_number()

#3
def table_lst(n=(1, 10)):
    start, end = n
    for i in range(start, end + 1):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

table_lst()

#4
def one_start(n):
    for i in range(n, 0, -1):
        print(i)
    print("Пуск!")

one_start(5)