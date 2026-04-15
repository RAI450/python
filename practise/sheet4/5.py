# Assignment 5: Salary Breakdown

# An employee wants to calculate salary per day and per hour.

# Input:
# Monthly salary = 36000
# Working days = 24
# Working hours per day = 8

# Expected Output:
# Salary per day = 1500.0
# Salary per hour = 187.5


sal,day,hrs=map(int,input("enter monthly salary,working days,working hours per day").split())
print(F"salary per day = {sal/day}\n salary per hour ={sal/(day*hrs)}")