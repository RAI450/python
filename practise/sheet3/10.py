# Assignment 10: Percentage Calculator

# Write a Python program that:

# Accepts total marks and obtained marks.
# Calculates percentage.

# Input:
# Total = 500
# Obtained = 400

# Output:
# Percentage = 80%

tm,ob=map(int,input("enter total marks and obtained marks").split())
percentage=ob*100/tm
print("percentage =",percentage,"%")