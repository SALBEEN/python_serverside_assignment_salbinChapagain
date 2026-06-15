# Program to store student names in a file and read i

students = []
print("Enter student names (type 'done' when finished):")

while True:
    name = input("> ")
    if name.lower() == "done":
        break
    if name.strip() != "":  
        students.append(name)

file_name = "students.txt"

with open(file_name, "w") as file:
    for student in students:
        file.write(student + "\n")

print("\n Names have been saved to " + file_name + "!")
print("-" * 30)


print("Reading names from the file:")
try:
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file could not be found.")