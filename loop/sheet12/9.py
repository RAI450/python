# 9.Step Difference Number Analyzer

# A mathematics research center studies hidden patterns inside numbers.
# For every entered number, the system compares adjacent digits step by step.
# Write a program to:

# Find the absolute difference between every pair of adjacent digits
# Display all step differences
# Find the sum of all step differences
# Find the largest step difference
# If the sum of step differences is divisible by the number of digits, print Balanced Number
# Otherwise print Unbalanced Number

# Use loops wherever required.

# Input:
# 57294
# Output:
# Step Differences: 2 5 7 5
# Sum = 19
# Largest = 7
# Unbalanced Number

num=int(input("enter the number "))


n=len(str(num))
a=num%10
sum=0
dif=""
for i in range(1,n):
    num=num//10
    b=num%10
    sd=abs(a-b)
    dif=dif+str(sd)
    sum=sum+sd
    a=b
rsd=""
dif=int(dif)
while dif>0:
    u=dif%10
    rsd=rsd+str(u)
    dif=dif//10
print(rsd)
print("sum = ",sum)
lar=0
for i in rsd:
    if int(i)>=lar:
        lar=int(i)
print("largest = ",lar)
if sum%(n-1)==0:
    print("balanced number")
else:
    print("unbalanced number")









# l=len(str(num))
# a=num//(10**(l-1))
# sd=""
# sum=0
# print(a)
# for i in range(1,l):
#     num=num-(a*(10**(l-i)))
#     b=num//(10**(l-i))
#     dif=abs(a-b)
#     sum=sum+dif
#     a=b
#     sd=sd+str(dif)
# print("step difference = ",sd)
# print("sum = ",sum)
