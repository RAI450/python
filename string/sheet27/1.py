# 1. Remove All Special Characters from a String

# Online Banking Customer Data Cleaning System

# A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

# Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

# * Alphabets
# * Numbers
# * Spaces

# The cleaned value should be stored back into the original string variable.

# Input:

# Deepika@@ Padukone!! 123
# Output:
# Deepika Padukone 123
# Input:
# Ajay###Singh$$$
# Output:
# AjaySingh

n=input("enter the details: ")

s=""
for i in n:
    a=ord(i)
    if (a>=65 and a<=90) or (a>=97 and a<=122) or (a>=48 and a<=57) or i==" ":
        s=s+i
print(s)