# QUESTION 2: STUDENT RESULT PROCESSING
# =====================================

# A training institute wants to manage student records using NamedTuple.

# Fields:
# roll_no, name, course, marks

# Requirements:

# 1. Read N student records from the user and store them in a list of NamedTuples.

# 2. Display all student details.

# 3. Find and display the topper of the class.

# 4. Count and display the number of students scoring above 80 marks.

# 5. Calculate and display the average marks.

# 6. Accept a course name from the user and display all students enrolled in that course.


# Test Case:

# Input:
# Enter number of students: 4

# 1 Ravi Python 85
# 2 Anjali Java 78
# 3 Karan Python 92
# 4 Pooja Testing 88

# Enter course: Python

# Expected Output:
# Topper:
# 3 Karan Python 92

# Students Above 80:
# 3

# Average Marks:
# 85.75

# Students in Python Course:
# 1 Ravi Python 85
# 3 Karan Python 92

from collections import namedtuple

stu=namedtuple("stu",["roll_no","name","course","marks"])

n=int(input("enter the number of students: "))

stud=[]
for i in range(1,n+1):
    roll=int(input("enter the roll no for student "+str(i)+" :"))
    nm=input("enter the name for student "+str(i)+" :")
    crse=input("enter the course for student "+str(i)+" :")
    mrk=int(input("enter the marks for student "+str(i)+" :"))
    stud.append(stu(roll,nm,crse,mrk))

for i in stud:
    print(i.roll_no ,i.name,i.course,i.marks)


count=0
top=stud[0]
add=0

for i in stud:
    if i.marks>top.marks:
        top=i
    if i.marks>80:
        count+=1
    add+=i.marks

print("topper of the class  is: ",top.roll_no,top.name,top.course,top.marks)

print("students above 80: ",count)
print("average marks: ",add/n)

cor=input("enter the course: ")

for i in stud:
    if i.course==cor:
        print(i.roll_no ,i.name,i.course,i.marks)

