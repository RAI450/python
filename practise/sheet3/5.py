# Assignment 5: Average Marks Calculator

# Write a Python program that:

# Accepts marks of 3 subjects.
# Calculates average.

# Input:
# Marks = 80, 90, 70

# Output:
# Average = 80.0

m1,m2,m3=map(int,input("enter marks of 3 subjects").split())
avg=(m1+m2+m3)/3
print("average =",avg)