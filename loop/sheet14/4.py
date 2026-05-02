# 4.Unique Digit Security Scanner

# A smart locker accepts only numbers whose all digits are unique.

# Write a program using for-else loop to:

# - Check every digit
# - If any repeated digit found reject
# - Else accept

# Input:
# 57294

# Output:
# Valid Unique Code

n=int(input("enter the number "))

# l=len(str(n))

# for i in range(1,l+1):
#     a=n%10


n2=n
a=n2%10
n2=n2//10
x=True
while n2>0:
    for i in str(n2):
        if int(i)==a:
            x=False
            n2=0                  # bad logic--- 
            break
    else:
        a=n2%10
        n2=n2//10
if x==True:
    print("valid unique number")
else:
    print("rejected")

