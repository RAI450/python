# 5.

# Automorphic Number Lock

# A high-security digital locker validates access codes using a special mathematical rule.

# When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
#  If it matches, the code is considered valid.

# An Automorphic Number is a number whose square ends with the same number.

# Task:
# Write a Python program to check whether a given number is an Automorphic Number or not.

# Example:
# Input:
# 25

# Output:
# Automorphic Number

n=int(input("enter the number"))

an=n**2
for i in str(n):
    if n%10!=an%10:
        print("not a automorphic number")
        break
    n=n//10
    an=an//10
else:
    print("automorphic number")

        

