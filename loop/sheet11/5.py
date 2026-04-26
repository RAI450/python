# 5. Count Factors of Number
# A mathematics learning app gives practice questions where students must know how many factors a number has.
# The app should automatically count the total factors of the entered number.
# Write a program to count total factors of a number using loops.

# Input:
# 12

# Output:
# Factors Count = 6

num=int(input("enter the number "))

count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print("factors count = ",count)

# count=1                             # optimized version-- the no. itself always be divisible by it
# for i in range(1,(num//2)+1):
#     if num%i==0:
#         count+=1
# print("factors count = ",count)