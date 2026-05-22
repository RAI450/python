# 5. Find the Number of Unique Characters in a String

# Password Strength Analyzer

# A cybersecurity company checks password strength based on the number of unique characters present.

# Passwords containing more unique characters are considered more secure.

# Write a Python program to count the number of unique characters in a string.

# Input:


# aabbccdde


# Output:


# 5

n=input("enter the password: ")

vis=""
count=0
for i in n:
    if i not in vis:
        vis=vis+i
        count+=1
print(count)