# Question 1: Employee Salary Management System
# Scenario

# A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

# Requirements

# Create a class named Employee with the following attributes:

# employee_id
# employee_name
# basic_salary

# Initialize the values using a constructor.

# Calculations
# HRA = 20% of Basic Salary
# DA = 15% of Basic Salary
# Gross Salary = Basic Salary + HRA + DA
# Sample Input
# Enter Employee ID : E101
# Enter Employee Name : Rahul Sharma
# Enter Basic Salary : 50000
# Sample Output
# ------ Employee Salary Details ------
# Employee ID      : E101
# Employee Name    : Rahul Sharma
# Basic Salary     : 50000.0
# HRA              : 10000.0
# DA               : 7500.0
# Gross Salary     : 67500.0

class employee:
    def __init__(self,id,name,sal):
        self.employee_id=id
        self.employee_name=name
        self.basic_salary=sal


    def hra(self):
        return 0.2*(self.basic_salary)
    def da(self):
        return 0.15*(self.basic_salary)
    def gs(self):
        return self.basic_salary+self.hra()+ self.da()
    
    
    def display(self):
        print("------ Employee Salary Details ------")
        print("Employee Id    : ",self.employee_id)
        print("Employee name    : ",self.employee_name)
        print("Basic Salary    : ",self.basic_salary)
        print("Hra     : ",self.hra())
        print("DA     : ",self.da())
        print("Gross Salary     : ",self.gs())
    

id=int(input("enter the id: "))
name=input("enter the name: ")
sal=int(input("enter the salary: "))

s1=employee(id,name,sal)
s1.display()









