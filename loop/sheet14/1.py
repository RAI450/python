# 1. Triple Operation Prime Verification System

# A cybersecurity company generates a security score from entered access code.

# Write a program to:

# - Find sum of digits of the number
# - Reverse the number
# - Find absolute difference between original number and reverse
# - Add digit sum and difference
# - Check whether final result is Prime or Not Prime

# Input:
# 4215

# Output:
# Sum of Digits = 12
# Reverse = 5124
# Difference = 909
# Final Result = 921
# Not Prime

num=int(input("enter the number "))                           
r=num
l=len(str(num))
rnum=""
sum=0
for i in str(num):
    sum=sum+int(i)
    a=num%10
    rnum=rnum+str(a)
    num=num//10
rnum=int(rnum)
dif=abs(rnum-r)
res=dif+sum
print("sum of digits = ",sum)
print("reverse = ",rnum)
print("difference = ",dif)
print("final result = ",res)

if res>1:                                    # using for-else block for checking prime
    for i in range(2,(res//2)+1):        
        if res%i==0:
            print("not prime")
            break
    else:
        print("prime number")
else:
    print("not prime")



# if res>1:                                   # without using for- else block for checking prime
#     x=True
#     for i in range(2,(res//2)+1):
#         if res%i==0:
#             print("not prime")
#             x=False
#             break
#     if x==True:
#         print("prime number")
# else:
#     print("not prime")

