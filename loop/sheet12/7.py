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

num=int(input("enter the number "))
count=0
                                              #0123======not printing rejected number
for i in range(1,2):
    if i==0:
        print("rejected number")
    else:
        for i in str(num):
            if int(i)==0:
                count+=1
        
if count==1:
    print("duck number")