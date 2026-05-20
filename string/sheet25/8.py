# 8.
# Airport Passenger Name Formatting System

# An international airport is developing an automated passenger management system. Many passengers enter their details in different formats such as lowercase, uppercase, mixed-case letters, and numbers while booking flight tickets online.

# Due to inconsistent formatting, problems occur while generating boarding passes, security verification records, and passenger identity reports.

# To solve this issue, the airport authority wants a program that automatically converts only the first character of every word into uppercase while keeping all remaining characters unchanged.

# The input may contain:
# - Passenger names
# - Passport details
# - Terminal names
# - Seat numbers
# - City names
# - Mixed uppercase/lowercase letters
# - Digits

# Task:
# Read a complete string from the user and convert the first character of every word into uppercase.

# Conditions:
# - Words may contain spaces
# - Digits should remain unchanged
# - Do not use built-in title() function

# Input:
# Enter passenger details:
# deepika padukone flight ai202 terminal 3 mumbai

# Output:
# Formatted Details:
# Deepika Padukone Flight Ai202 Terminal 3 Mumbai


# Test Case 2:
# Input:
# Enter passenger details:
# DEEPIKA pADukone gate number 12

# Output:
# Formatted Details:
# DEEPIKA PADukone Gate Number 12


# Test Case 3:
# Input:
# Enter passenger details:
# international departure terminal delhi airport

# Output:
# Formatted Details:
# International Departure Terminal Delhi Airport


# Test Case 4:
# Input:
# Enter passenger details:
# business class passenger seat b12

# Output:
# Formatted Details:
# Business Class Passenger Seat B12


n=input("Enter passenger details: ")

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