# 8. Largest Smallest Sum Prime Checker

# A number analyzer finds largest and smallest digit.

# Write a program to:

# - Find largest digit
# - Find smallest digit
# - Find sum of both
# - Check whether sum is Prime or Not

# Input:
# 57294

# Output:
# Largest = 9
# Smallest = 2
# Sum = 11
# Prime

num=int(input("enter number "))
dn=num
s=9
l=0
while dn>0:
    a=dn%10
    if a>=l:
        l=a
    dn=dn//10
while num>0:
    a=num%10
    if a<=s:
        s=a
    num=num//10
print("largest = ",l)
print("smallest = ",s)
print("sum = ",s+l)
sum=s+l
x=True
for i in range(2,(sum//2)+1):
    if sum%i==0:
        x=False
        break

if x==True:
    print("prime")
else:
    print("not prime")




    