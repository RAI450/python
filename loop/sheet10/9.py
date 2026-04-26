# *9. Check All Digits Are Even*
# A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
# Write a program to *check whether all digits of a number are even using loops*.

# Input: 2468
# Output: All Even

# Input: 2456
# Output: Not All Even

n=int(input("enter the no"))
a=True
while n>0 and a==True:
    if (n%10)==2:
        a=True
    else:
        a=False
    n=n//10
if a==True:
    print("all are even")
else:
    print("not even")
