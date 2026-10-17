login = input('введите логин: ')
password = input('введите пароль: ')
age = input('введите возраст: ')

correct_login = "python_student"
correct_password =  "FullCode2026"
correct_age = age

if correct_login == login.lower() and login.strip():
    if correct_password == password:
        if int(age) >= 18:
            print("Добро пожаловать!")
        else:
            print('Доступ разрешен только с 18')
    else:
        print('Неверный логин')
else:
    print('Неверный пароль')
