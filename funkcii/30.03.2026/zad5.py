students = [
    {"name": "mar", "grade": 5.50, "age": 17},
    {"name": "maa", "grade": 4.50, "age": 17},
    {"name": "mas", "grade": 3.50, "age": 17}
]
ssdnts = sorted(students, key=lambda x: x["grade"], reverse=True)

for s in ssdnts:
    print(f"{s['name']} {s['grade']}")
