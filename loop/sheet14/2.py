# 2. Multi Stage Prime Lock System

# A smart locker opens only if final derived number is prime.

# Write a program to:

# - Find sum of digits
# - Find product of digits
# - Find difference between product and sum
# - Count digits in difference
# - Add digit count to difference
# - Check whether final result is Prime or Not

# Input:
# 234

# Output:
# Sum = 9
# Product = 24
# Difference = 15
# Digits = 2
# Final Result = 17
# Prime

# for i in range(1,10):
#     print(i)
#     if i==5:
#         break
# else:
#     print("no break")

n=int(input("enter the number "))

sum=0
pro=1

for i in str(n):
    sum=sum+int(i)
    pro=pro*int(i)

print("sum = ",sum)
print("product = ",pro)
dif=abs(pro-sum)
print("difference = ",dif)
l=len(str(dif))
print("digits = ",l)
res=dif+l
print("final result = ",res)

if res>1:
    for i in range(2,(res//2)+1):        
        if res%i==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")






