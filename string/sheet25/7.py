# 7.
# Smart City Citizen Information Formatter

# The Smart City Management Department is developing a digital portal to store citizen information in a professional format. Many citizens enter their details using small letters, uppercase letters, mixed casing, or numbers, which creates problems while generating official documents like ID cards, electricity bills, tax records, certificates, and address proofs.

# To solve this issue, the department wants a program that automatically converts only the first character of every word into uppercase while keeping the remaining characters unchanged.

# The input may contain:
# - Words already written in uppercase
# - Mixed-case words
# - Numbers
# - Address details
# - Department names
# - City names

# Task:
# Read a complete string from the user and convert the first character of every word into uppercase.

# Conditions:
# - Words may contain spaces between them
# - Do not use built-in title() function
# - Digits should remain unchanged

# Input:
# Enter citizen information:
# deepika padukone from smart city raisen madhya pradesh

# Output:
# Formatted Information:
# Deepika Padukone From Smart City Raisen Madhya Pradesh


# Test Case 2:
# Input:
# Enter citizen information:
# DEEPIKA pADukone ward number 12

# Output:
# Formatted Information:
# DEEPIKA PADukone Ward Number 12


# Test Case 3:
# Input:
# Enter citizen information:
# government engineering college bhopal zone 3

# Output:
# Formatted Information:
# Government Engineering College Bhopal Zone 3


# Test Case 4:
# Input:
# Enter citizen information:
# python FULL stack developer batch 18

# Output:
# Formatted Information:
# Python FULL Stack Developer Batch 18


n=input("Enter citizen information: ")

count=0
for i in n:
    count+=1
new=""

if ord(n[0])>=97 and ord(n[0])<=122:
    new=new+chr(ord(n[0])-32)
else:
    new=new+n[0]

for i in range(1,count):
    if ord(n[i])>=97 and ord(n[i])<=122 and n[i-1]==" ":
        new=new+chr(ord(n[i])-32)
    else:
        new=new+n[i]
print("Formatted Details: ",new)