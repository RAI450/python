# 1. Prime Security Code Checker

# A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
# only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

# When an employee enters a code, the system must verify whether the number is prime.
# If yes, access is granted; otherwise, access is denied.

# Write a program to check whether the entered number is Prime or Not Prime.

# Input:
# 29

# Output:
# Prime Number

num=int(input("enter number "))

a=False                              # best logic for prime is assume the given no. is prime(a=true)
i=2                                     
while i<=num/2:
    if num%i==0:
        a=False
        break
    else:
        a=True
        i+=1
if a==True:
    print("prime number")
else:
    print("not a prime number")



# a=True                               #          using for
# for i in range(2,(num//2)+1):
#     if num%i==0:
#         a=False
#         break
# if a==True:
#     print("prime number")
# else:
#     print("not a prime number")
        