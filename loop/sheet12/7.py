# 7. Duck Number Checker

# A verification system is used by an e-commerce company to validate promotional coupon numbers.
# Coupon numbers containing at least one zero in between digits are considered special duck numbers.
# However, if the number starts with zero, it is rejected immediately.

# A duck number is a number that contains at least one zero but does not start with zero.

# Example:
# 1023

# Write a program using loops to check whether the entered number is a Duck number.

# Input:
# 1023

# Output:
# Duck Number

num=input("enter the number ")
a=len(num)-1
num=int(num)
count=0
if num//(10**a)==0:
    print("number rejected ")
else:
    for i in str(num):
        if int(i)==0:
            count+=1
    if count>0:
        print("duck number")
    else:
        print("not duck number")
