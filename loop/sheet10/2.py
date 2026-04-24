# 2. Factorial of a Number
# In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. 
# Factorial of a number n is the product of all numbers from 1 to n.
# Write a program to calculate the *factorial of a given number using loops*.

# Input: n = 5
# Output: Total Ways = 120

n=int(input("enter number "))
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print("total ways = ",fact)


