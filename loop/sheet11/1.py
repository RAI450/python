# 1. Largest Digit in Number
# A cybersecurity company checks numeric passwords used in smart lockers.
# To identify password strength, the system finds the highest digit present in the entered password. 
# Higher digits indicate stronger variation in the password pattern.
# Write a program to find the largest digit in a number using loops.

# Input:
# 57294

# Output:
# Largest Digit = 9

num=int(input("enter number"))

a='0'                   #using for loop 
for i in str(num):
    if i>a:
        a=i
print("largest digit = ",a)

# a=0                      #using loop but comparing in integers not string
# for i in str(num):
#     if int(i) > a:
#         a=int(i)
# print("largest digit = ",a)


# a=0                    #using while loop
# while num>0:
#     mod=num%10
#     if mod>a:
#         a=mod
#     num=num//10
# print("largest digit = ",a)
