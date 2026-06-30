# recursion:
# Assignment 1: Smart Street Lights (Fibonacci Series)

# A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

# Month 1 → 0 lights
# Month 2 → 1 light
# Every following month, the number of lights installed is the sum of the previous two months.

# As a software developer, your task is to help the city planning department generate the installation schedule.

# Task

# Write a recursive function to print the first N Fibonacci numbers.

# Input
# Enter the number of months:
# 7
# Output
# 0 1 1 2 3 5 8

n=int(input("enter the number number of months: "))

x=0
l=[]
def add(a,b):
    if x==n-2:
        return a+b
    
        

