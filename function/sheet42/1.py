# 1.
# Employee Record Sorting (Lambda)


# A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

# Task

# Write a Python program to sort the employee records(sal) using a lambda expression.

# Input
# employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
# Output
# [('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]


n=int(input("enter the number of employee: "))
emp=[]
for i in range(n):
    s=()
    nm=input("enter the name: ")
    s=int(input("enter the salary: "))
    s=(nm,s)
    emp.append(s)

emp.sort(key=lambda x:x[1])
print(emp)

