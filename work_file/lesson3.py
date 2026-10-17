import json

user = {"name": "Aman", "age": 25, "city": "Bishkek"}
with open("u.json", "w") as f:
    json.dump(user, f)

student = {"name": "Aisuluu", "course": 2}
s = json.dumps(student)
print(f"S: {s}")

with open("u.json", "r") as f:
    res_f = json.load(f)
print(f"F: {res_f}")

res_s = json.loads(s)
print(f"D: {res_s}")
