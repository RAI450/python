# 1. Product of Odd Numbers up to N

# A puzzle game rewards players by multiplying odd numbers up to n.
# Write a program using loops to find product of odd numbers.

# Input:
# 5

# Output:
# 15

num=int(input("enter the number "))
pro=1
for i in range(1,num+1,2):
    pro=pro*i

print(pro)