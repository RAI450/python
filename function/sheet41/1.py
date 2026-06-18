# 1.
# STUDENT RESULT MANAGEMENT SYSTEM

# Scenario:

# A college examination department wants to automate the process of generating student results. The staff should be able to enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

# Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

# MENU

# 1. Add Student Details
# 2. Calculate Total Marks
# 3. Calculate Percentage
# 4. Find Grade
# 5. Display Complete Result
# 6. Find Highest Subject Mark
# 7. Find Lowest Subject Mark
# 8. Exit

# Functional Requirements

# 1. Add Student Details

#    * Student Name
#    * Roll Number
#    * Marks of 5 Subjects

# 2. Calculate Total Marks

# 3. Calculate Percentage

# 4. Find Grade

# 5. Display Complete Result

# 6. Find Highest Subject Mark

# 7. Find Lowest Subject Mark

# 8. Exit

# Grade Criteria

# Percentage        Grade

# 90 - 100          A+
# 80 - 89           A
# 70 - 79           B
# 60 - 69           C
# 50 - 59           D
# Below 50          Fail

# Constraints

# * Marks should be between 0 and 100.
# * Display an appropriate message for invalid marks.
# * The program should continue until the user chooses Exit.

# Sample Input / Output

# *** STUDENT RESULT MANAGEMENT ***

# 1. Add Student Details
# 2. Calculate Total Marks
# 3. Calculate Percentage
# 4. Find Grade
# 5. Display Result
# 6. Find Highest Mark
# 7. Find Lowest Mark
# 8. Exit

# Enter Choice : 1

# Enter Student Name : Ajay
# Enter Roll Number : 101

# Enter Mark 1 : 78
# Enter Mark 2 : 85
# Enter Mark 3 : 92
# Enter Mark 4 : 88
# Enter Mark 5 : 77

# Student details added successfully.

# Enter Choice : 2

# Total Marks = 420

# Enter Choice : 3

# Percentage = 84.0

# Enter Choice : 4

# Grade = A

# Enter Choice : 6

# Highest Mark = 92

# Enter Choice : 7

# Lowest Mark = 77

# Enter Choice : 5

# ----------- RESULT CARD -----------

# Name        : Ajay
# Roll Number : 101

# Marks
# Subject 1 : 78
# Subject 2 : 85
# Subject 3 : 92
# Subject 4 : 88
# Subject 5 : 77

# Total Marks : 420
# Percentage  : 84.0
# Grade       : A
# Highest Mark: 92
# Lowest Mark : 77

# Enter Choice : 8

# Thank You. Program Terminated.

# Important Instructions

# 1. The solution must be developed using multiple user-defined functions.
# 2. Use appropriate parameters wherever data needs to be passed between functions.
# 3. Use return statements wherever a function needs to send a result back to the caller.
# 4. Avoid using unnecessary global variables.
# 5. Implement the application using a menu-driven approach.
# 6. Perform proper input validation.
# 7. Write meaningful function names and maintain proper code readability.
# --------------------------------------------------------

def add(mark):
    s=0
    for i in mark:
        s+=i
    return s

def per(m):
    perc=(m*100)/500
    return perc
def grad(p):
    if p>=90 and p<=100:
        c="A+"
    elif p<=89 and p>=80:
        c="A"
    elif p<=79 and p>=70:
        c="B"
    elif p<=69 and p>=60:
        c="C"
    elif p<=59 and p>=50:
        c="D"
    else:
        c="Fail"
    return c

mark=[]
while True:
    print("""--------------------------
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
    -------------------------------------      """)
    n=int(input("enter the choice: "))
    
    match n:

        case 1:
            nm=input("enter the name: ")
            rol=int(input("enter the roll no: "))
            
            
            for i in range(5):
                c=int(input("enter mark "+(str(i+1))+": "))
                if c>=0 and c<=100:
                    mark.append(c)
                else:
                    print("you enter wrong marks")
                    break
            
            print("Student details added successfully.")

        case 2:
            m=add(mark)
            print("total marks: ",m)
        
        case 3:
            p=per(m)
            print("percentage: ",p)
        
        case 4:
            g=grad(p)
            print("Grade = ",g)

        case 5:
            print("----------- RESULT CARD -----------")
            print("NAME         : ",nm)
            print("ROLL NUMBER  : ",rol)
            print()
            print("marks")
            for i in range(5):
                print("subject ",i+1," : ",mark[i])
            print()
            print("total marks      : ",m)
            print("total percentage : ",p)
            print("grade            : ",g)
            print("highest mark     : ",high)
            print("lowest mark      : ",sml)
        case 6:
            high=0
            for i in mark:
                if i>high:
                    high=i
            print("Highest Mark = ",high)
        case 7:
            sml=mark[0]
            for i in mark:
                if i<sml:
                    sml=i
            print("Lowest Mark = ",sml)

        case 8:
            print("Thank You. Program Terminated.")
            break

        case _:
            print("invalid choice please choose again")
