# def loop(x, y):
#     for i in range(x, y):
#         if i == 10:
#             print(i)
# loop(0, 20)


name = ["Asan", "Uson", "Sadyr", "Bermet", "Alina", "Adina"]

def index_name():
    n = int(input("введи число: "))
    idx = name[n]
    print(idx)
    return idx

def reverse_name(idx):
    rev = idx[::-1]
    print(idx + " = " + rev)

def change_name():
    idx = int(input("введи индекс: "))
    new_name = input("задай новое имя: ")
    name[idx] = new_name
    print(name)

def append_name():
    add_name = input("нужно новое имя: ")
    name.append(add_name)
    print(name)


c = index_name()
reverse_name(c)
change_name()
append_name()
