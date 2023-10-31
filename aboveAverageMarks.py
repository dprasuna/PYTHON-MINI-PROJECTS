number_of_students = int(input("Please enter the number of students: "))

allMarks = []
totalMarks = 0

for i in range(0,number_of_students):
    nextStudent = int(input(f"Enter your marks: "))
    allMarks.append(nextStudent)
    totalMarks += nextStudent


avgMarks = round(totalMarks / number_of_students, 2)
print(f"\n Average marks of the students: {avgMarks}")

aboveAvgMarks = []
aboveAvgMarksCount = 0
for i in allMarks:
    if i > avgMarks:
        aboveAvgMarks.append(i)
        aboveAvgMarksCount += 1

print(f"{aboveAvgMarksCount} students has above average marks: {aboveAvgMarks}")

