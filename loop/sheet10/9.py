# *9. Check All Digits Are Even*
# A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
# Write a program to *check whether all digits of a number are even using loops*.

# Input: 2468
# Output: All Even

# Input: 2456
# Output: Not All Even

n=int(input("enter number "))
out=True
while out==True and n>0:
    mod=n%10
    n=n//10
    if mod%2==0:
        out=True
    else:
        out==False

if out==True:
    print("Output: All Even")
else:
    print("Output: Not All Even")
    


