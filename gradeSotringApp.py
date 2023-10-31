print("Welcome to the Grade Sorting App")

print("Enter your grades (0-100)")

grades = []
while len(grades) < 4:
    grade = int(input("Enter your grade: "))
    grades.append(grade)

print(f"\nYour grades are {grades}")

grades.sort(reverse=True)
print(f"\nYour grades in highest to lowest order: {grades}")

topGrades = []
for grade in grades:
    if grade > 75:
        topGrades.append(grade)

print(f"\n Your best grades are: {topGrades}")