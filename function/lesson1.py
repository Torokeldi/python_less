def calc():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    sym = input("enter symbol: ")

    if sym == "+":
        print(num1 + num2)
    if sym == "-":
        print(num1 - num2)
    if sym == "%":
        print(num1 % num2)
    if sym == "*":
        print(num1 * num2)
    if sym == "/":
        print(num1 / num2)
    if sym == "//":
        print(num1 // num2)
    if sym == "**":
        print(num1 ** num2)
calc()


def addition(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiple(a, b):
    return a * b
def divide(a, b):
    return a / b

calculator = {
    "+": addition,
    "-": substraction,
    "*": multiple,
    "/": divide
}

a = int(input("введите число: "))
b = int(input("введите другое число: "))

print(calculator[input("операция: ")](a, b))