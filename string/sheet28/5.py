# 5.
# Cybercrime Log Analysis System

# A cybersecurity company monitors encrypted login activity stored as character-based security logs.

# During investigation, analysts need to identify the last character that repeats in the log sequence.
# This helps detect the most recent duplicated activity pattern before a possible security breach.

# Write a Python program to find the last repeating character in a given string.

# If no repeating character exists, print:

# No repeating character found
# Input:
# abccdbefga
# Output:
# a

n=input("enter the string: ")

l=len(n)
flag=1
for i in range(-1,-l,-1):
    if flag==1:
        for j in range(i-1,-l-1,-1):
            if n[i]==n[j]:
                res=n[j]
                flag=0
                break
if flag==1:
    print("no repeating character found ")
else:
    print(res)

    

        