student = {
    "name": "Krishna",
    "age": 21,
    "branch": "AIML",
    "college": "ICEEM"
}

print("Name:", student["name"])
print("Branch:", student["branch"])

student["city"] = "Aurangabad"

print("Student Details:")

for key, value in student.items():
    print(key, ":", value)