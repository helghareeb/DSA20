# بسم الله الرحمن الرحيم

from array_two_d import MyArrayTD

# Open the text file for reading
grades_file = open('py_code/grades.txt', 'r')

# Extract the first two values; indicate the size of the array
num_students = int(grades_file.readline())
num_exams = int(grades_file.readline())

# Create the 2-D Array to store the grades
exam_grades = MyArrayTD(num_students, num_exams)

# Extract the grades from the remainig lines
i = 0
for student in grades_file:
    grades = student.split()
    for j in range(num_exams):
        exam_grades[i,j] = int(grades[j])
    i += 1

# Close the text file
grades_file.close()

# Compute each student's average exam grade
for i in range(num_students):
    total = 0
    for j in range(num_exams):
        total += exam_grades[i,j]
    exam_avg = total / num_exams

    print( "%2d:  %6.2f" % (i+1, exam_avg) )

