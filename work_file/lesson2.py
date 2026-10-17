import csv

students_data = [
    ["Бермет", 18],
    ["Данияр", 19],
    ["Жумабек", 20]
]

with open('students.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["аты", "жашы"])
    writer.writerows(students_data)

new_students = []
while True:
    name = input("атын жаз: ")
    if name == "0":
        break

    age = int(input("жашын жаз: "))
    new_students.append([name, age])

if new_students:
    with open('students.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_students)
    print(f"{new_students} кошулду")

with open('students.csv', mode='r') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)
    total_students = len(rows)

print(f"жалпы сан: {total_students}")
