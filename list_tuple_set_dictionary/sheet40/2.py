# 2.

# ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

# A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

# Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

# The system should store student records in a nested dictionary where:

# Key → Student ID
# Value → Dictionary containing student information

# Each student record should contain:

# Student Name
# Course Name
# Mobile Number
# Fees
# City
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "course":"Python",
#     "mobile":"9876543210",
#     "fees":25000,
#     "city":"Indore"
# },
# 102:{
#     "name":"Ravi",
#     "course":"Java",
#     "mobile":"9876500000",
#     "fees":22000,
#     "city":"Bhopal"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =========================================
#  STUDENT MANAGEMENT SYSTEM
# =========================================

# 1. Add New Student
# 2. Search Student
# 3. Update Course
# 4. Delete Student
# 5. Display All Students
# 6. Count Total Students
# 7. Display Students By Course
# 8. Display Students By City
# 9. Find Student Paying Highest Fees
# 10. Find Student Paying Lowest Fees
# 11. Exit
# Functional Requirements
# 1. Add New Student

# Accept the following details:

# Student ID
# Student Name
# Course Name
# Mobile Number
# Fees
# City

# Store the information in the nested dictionary.

# Validation

# If Student ID already exists:

# Student ID Already Exists
# 2. Search Student

# Accept Student ID from the user.

# If found, display complete student information.

# Sample Output
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Mobile     : 9876543210
# Fees       : 25000
# City       : Indore

# If not found:

# Student Not Found
# 3. Update Course

# Accept Student ID.

# If found:

# Ask for new course name.
# Update the course.
# Sample Output
# Course Updated Successfully
# 4. Delete Student

# Accept Student ID.

# If found:

# Delete the record.
# Sample Output
# Student Deleted Successfully

# Otherwise:

# Student Not Found
# 5. Display All Students

# Display all student records in a proper format.

# Sample Output
# -----------------------------------
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Fees       : 25000
# -----------------------------------

# Student ID : 102
# Name       : Ravi
# Course     : Java
# Fees       : 22000
# -----------------------------------
# 6. Count Total Students

# Display total number of students enrolled.

# Sample Output
# Total Students : 45
# 7. Display Students By Course

# Accept a course name from the user.

# Display all students enrolled in that course.

# Sample Output
# Enter Course : Python

# 101  Ajay
# 105  Neha
# 112  Aman

# If no students are found:

# No Students Found
# 8. Display Students By City

# Accept city name from the user.

# Display all students belonging to that city.

# Sample Output
# Enter City : Indore

# 101  Ajay
# 108  Ravi
# 115  Pooja
# 9. Find Student Paying Highest Fees

# Display complete details of the student who has paid the highest fees.

# Sample Output
# Highest Fee Paying Student

# Student ID : 121
# Name       : Neha
# Course     : Data Science
# Fees       : 50000
# 10. Find Student Paying Lowest Fees

# Display complete details of the student who has paid the lowest fees.

# Sample Output
# Lowest Fee Paying Student

# Student ID : 131
# Name       : Aman
# Course     : React
# Fees       : 15000
# 11. Exit

# Terminate the application.

# Sample Output
# Thank You For Using Student Management System



dt={}


while True:
    print("""
    =====================================
        STUDENT MANAGEMENT SYSTEM
    =====================================

    1. Add New Student
    2. Search Student
    3. Update Course
    4. Delete Student
    5. Display All Students
    6. Count Total Students
    7. Display Students By Course
    8. Display Students By City
    9. Find Student Paying Highest Fees
    10. Find Student Paying Lowest Fees
    11. Exit
        """)

    n=int(input("enter the choice: "))
   
    match n:
        case 1:
            print("adding new student---")
            
            id=int(input("enter the roll_number: "))
            if id not in dt:
                name=input("enter the name: ")
                cr=input("enter the course: ")
                mob=int(input("enter the mobile number: "))
                fees=int(input("enter the fees: "))
                city=input("enter the city: ")

                dt[id]={
                    "name": name,
                    "course": cr,
                    "mobile": mob,
                    "fees": fees,
                    "city": city
                }
                print("Student added successfully")
            else:
                print("Student ID Already Exists")
        
        case 2:
            id=int(input("enter the patient id: "))
            if id in dt:
                print("student id : ",id)
                for k,v in dt[id].items():
                    print(k,"   : ",v)
            else:
                print("Student ID not found")
        case 3:
            id=int(input("enter the student id: "))
            if id in dt:
                cnew=input("enter the new course: ")
                dt[id]["course"]=cnew
                print("course updated successfully")
            else:
                print("Student ID not found")

        case 4:
            id=int(input("enter the student id: "))
            if id in dt:
                del dt[id]
                print("student record deleted successfully")
            else:
                print("patient id not found")
        case 5:
            if len(dt) == 0:
                print("No students found")
            else:
                for i in dt:
                    print("---------------------------")
                    print("student id : ",i)
                    for k,v in dt[i].items():
                        print(k,"   : ",v)
                print("---------------------------")
        
        case 6:
            
            print("total students :",len(dt))
        
        case 7:
            crs=input("enter the course: ")
            flag=False
            for i in dt:
                if dt[i]["course"]==crs:
                    flag=True
                    print(i," ",dt[i]["name"])
            if flag==False:
                print("no student found")

        case 8:
            cty=input("enter the city: ")
            flag=False
            for i in dt:
                if dt[i]["city"]==cty:
                    flag=True
                    print(i," ",dt[i]["name"])
            if flag==False:
                print("no student found")

        case 9:
            if len(dt) == 0:
                print("No students found")
            else:
                p=0
                a=0
                for i in dt:
                    if dt[i]["fees"]>a:
                        a=dt[i]["fees"]
                        p=i
                print("highest fee student details")
                print("student id : ",p)
                for k,v in dt[p].items():
                        print(k,"   : ",v)
        case 10:
            if len(dt) == 0:
                print("No students found")
            else:
                p=0
                a=float('inf')
                for i in dt:
                    if dt[i]["fees"]<a:
                        a=dt[i]["fees"]
                        p=i
                print("lowest fee student details")
                print("student id : ",p)
                for k,v in dt[p].items():
                        print(k,"   : ",v)


        case 11:
            print("Thank you for using student management system")
            break
        case _:
            print("Invalid choice. Please enter 1 to 11.")




