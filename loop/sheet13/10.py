# 10.Zero Count Prime Scanner

# A banking system checks account numbers.

# Write a program to:

# - Count zero digits
# - Find sum of digits
# - Add zero count and sum
# - Multiply by smallest digit
# - Check whether final result is Prime or Not

# Input:
# 908406

# Output:
# Zero Count = 2
# Sum = 27
# Smallest Digit = 0
# Final Result = 0
# Not Prime

n=input("enter the number ")

count=0
sum=0
sml=9
for i in n:
    sum+=int(i)
    if int(i)==0:
        count+=1
        sml=int(i)
    else:
        if int(i)<=sml:
            sml=int(i)
print("zero count = ",count)
print("sum = ",sum)
print("smallest digit = ",sml)
tsum=count+sum
res=tsum*sml
print("final result = ",res)

if res>1:
    x=True
    for i in range(2,(res//2)+1):
        if res%i==0:
            x=False
            break
    if x==True:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime")

    
