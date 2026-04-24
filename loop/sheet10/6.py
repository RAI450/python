# 6. Armstrong Number (3-digit)
# In coding competitions, certain numbers are considered unique. 
# A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
# Write a program to *check whether a number is an Armstrong number using loops*.

# Input: 153
# Output: Armstrong

num=int(input("enter number "))
n=num
sum=0
while n>0:
    mod=n%10
    n=n//10
    sum=sum+(mod**3)
if sum==num:
    print("armstrong")
else:
    print("not armstrong")