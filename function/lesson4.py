def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))


def print_words(*args):
    print(", ".join(args))


print_words("Кыргызстан", "Казахстан", "Узбекистан", "Таджикистан")


def introduce(**kwargs):
    name = kwargs['name'] if 'name' in kwargs else 'Не указано'
    age = kwargs['age'] if 'age' in kwargs else 'Не указан'
    city = kwargs['city'] if 'city' in kwargs else 'Не указан'

    print(f"Привет! Меня зовут {name}, мне {age} лет, я из города {city}.")


introduce(name="Торогелди", age=25, city="Бишкек")


def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"# {key}: {value}")


person_info(name="Толик", hobby="чтение", pet="собака")


def show_info(*args, **kwargs):
    args_as_strings = [str(arg) for arg in args]
    print("args:", " ".join(args_as_strings))

    print("# kwargs:")
    for key, value in kwargs.items():
        print(f"# {key} = {value}")


show_info(1, 2, 3, name="Самат", age=20)


# # 1. SyntaxError
# if True
#     print("Этот код не запустится")
#
# # 2. IndentationError
# def greet():
# print("Привет!")

# 3. SyntaxError
# text = "Привет'
#
# # 4. SyntaxError
# class = "Мой класс"
#
# # 5. SyntaxError
# print("Забыли закрыть скобку"
#
# # 6. ZeroDivisionError
# result = 10 / 0
#
# # 7. NameError
# print(unknown_variable)

# 8. TypeError
# age = "Мне " + 25 + " лет"
#
# # 9. ValueError
# number = int("слово")
#
# # 10. IndexError
# my_list = [10, 20, 30]
# print(my_list[5])
#
# # 11. KeyError
# user = {"name": "Анна"}
# print(user["email"])
#
# # 12. AttributeError
# text = "привет"
# text.append("!")

