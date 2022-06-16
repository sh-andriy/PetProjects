student_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
print("The list of the students is", student_names)
search_name = input("Enter the name of the student: ")

for ind, name in enumerate(student_names):
    if name == search_name:
        print("The student", search_name, " is present in the class.")
        break
else:
    print("The student", search_name, " is absent from class.")
