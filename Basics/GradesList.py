grades = input("Enter the grades for the test: ").split()

for grade in sorted(set(grades)):
    print("Number of ratings {} = {}".format(grade, grades.count(grade)))