from datetime import datetime, timedelta

n = datetime.now()
t = timedelta()
print(n + t)

now = datetime.now()

print("Азыр:", now.strftime("%d.%m.%Y"))

print("Азыр:", now.strftime("%H:%M:%S"))

f = now + timedelta(days=30)
print("дата:", f.strftime("%d.%m.%Y"))

s = datetime(2026, 1, 1)
d = (now - s).days
print(f" {d} кун")

inp = input("Туулган кун: ")

try:
    birth = datetime.strptime(inp, "%d.%m.%Y")
    print(f"Туура: {birth}")
except ValueError:
    print("Ката")