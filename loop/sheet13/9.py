# 9.Even Odd Difference Prime System

# A smart scanner counts even and odd digits.

# Write a program to:

# - Count even digits
# - Count odd digits
# - Find difference
# - Check whether difference is Prime or Not

# Input:
# 123456

# Output:
# Even Count = 3
# Odd Count = 3
# Difference = 0
# Not Prime

n=int(input("enter number "))
a=n
even=0
odd=0
while a>0:
    b=a%10
    if b%2==0:
        even+=1
    else:
        odd+=1
    a=a//10
print("even count = ",even)
print("odd count = ",odd)
dif=abs(even-odd)
print("difference = ",dif)
if dif>1:
    x=True
    for i in range(2,(dif//2)+1):
        if dif%i==0:
            x=False
    if x==True:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime")
            
