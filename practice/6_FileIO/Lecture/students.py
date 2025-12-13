# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, home = line.rstrip().split(",")
#         print(f"{name} is in {home}")


# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         students.append(f"{name} is in {home}")

# for student in sorted(students):
#     print(student)

students = []
with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["home"] = home
        student = {"name": name, "home": home}
        students.append(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["home"]

# for student in sorted(students, key=get_name, reverse=False):
#     print(f"{student['name']} is in {student['home']}")

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
