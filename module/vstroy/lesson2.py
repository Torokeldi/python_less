import math, random, datetime, os, sys

inpint = float(input("num: "))
maxint = [12, 34, 56, 33, 22, 33, 11]
random_int = range(1, 10)
random_fruit = ["cherry", "apple", "banana", "orange", "grape", "mango", "pineapple"]
random_int2 = random.randint(1, 100)
inpbirth = input("birthday: ")

if random_int2 > 50:
    print(f"{random_int2} чон 50дон")
else:
    print(f"{random_int2} кичине 50дон")

print(math.sqrt(int(inpint)))
print(max(maxint))
print(math.ceil(inpint))
print(random.choice(random_int))
print(random.choice(random_fruit))
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%H.%M"))
birth_date = datetime.datetime.strptime(inpbirth, "%d.%m.%Y")
print(datetime.datetime.now() - birth_date)
print(os.name)
print(os.getcwd())
print(sys.version)
print(sys.platform)