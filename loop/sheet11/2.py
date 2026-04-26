# 2. Smallest Digit in Number
# A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
# Write a program to find the smallest digit in a number using loops.

# Input:
# 57294

# Output:
# Smallest Digit = 2

num=int(input("enter number"))

a='9'                   #using for loop 
for i in str(num):
    if i<=a:
        a=i
print("smallest digit = ",a)