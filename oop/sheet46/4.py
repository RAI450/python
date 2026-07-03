
# Question 4: Student Result Processing System
# Scenario

# A college wants to automate result generation by calculating total marks, percentage, and grade.

# Requirements

# Create a class named Student with:

# roll_number
# student_name
# marks1
# marks2
# marks3

# Initialize the values using a constructor.

# Calculations
# Total = Marks1 + Marks2 + Marks3
# Percentage = Total / 3
# Grade Criteria
# Percentage	Grade
# 90 and above	A
# 75 to 89	B
# 60 to 74	C
# Below 60	D
# Sample Input
# Enter Roll Number : 101
# Enter Student Name : Priya Sharma
# Enter Marks in Subject 1 : 85
# Enter Marks in Subject 2 : 90
# Enter Marks in Subject 3 : 88
# Sample Output
# ------ Student Result ------
# Roll Number      : 101
# Student Name     : Priya Sharma
# Total Marks      : 263
# Percentage       : 87.67
# Grade            : B


class student():
    def __init__(self,roll,name,m1,m2,m3):
        self.roll_number=roll
        self.student_name=name
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    
    def tot(self):
        return self.marks1 + self.marks2 + self.marks3
    def per(self):
        return (self.tot()/3)
    def gra(self):
        if self.per()>=90:
            return "A"
        elif self.per()>=75:
            return "B"
        elif self.per()>=60:
            return "C"
        else:
            return "D"
    
    def dis(self):
        print(" ------ Student Result ------")
        print("Roll Number   :  ",self.roll_number)
        print("student name   :  ",self.student_name)
        print("total marks   :  ",self.tot())
        print("percentage   :  ",self.per())
        print("grade   :  ",self.gra())

    

r=int(input("enter the roll number: "))
n=input("enter the name: ")
m1=int(input("enter the marks1: "))
m2=int(input("enter the marks2: "))
m3=int(input("enter the marks3: "))

s=student(r,n,m1,m2,m3)
s.dis()