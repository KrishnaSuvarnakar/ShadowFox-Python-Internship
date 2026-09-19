file = open("student.txt", "w")

file.write("Name: Krishna\n")
file.write("Branch: AIML\n")
file.write("College: ICEEM\n")

file.close()

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()