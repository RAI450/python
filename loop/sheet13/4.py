# 4. Prime Security Code Checker – Advanced

# A high-security lab accepts only prime numbered access codes.

# When a user enters a number, the software must:

# - Check whether number is prime
# - If prime, print next immediate prime number
# - If not prime, print previous immediate prime number

# Write a program using loops only.

# Input:
# 29

# Output:
# Prime Number
# Next Prime = 31

n=int(input("enter number "))
a=False
for i in range(2,(n//2)+1):
    if n%i==0:
        a=False
        break
    else:
        a=True
if a==True:
    print("prime number")
    while True:
        n=n+1
        b=False
        i=2
        while i<=n//2:
            if n%i==0:
                b=False
                break
            else:
                b=True
                i+=1
        if b==True:
            print("next prime number = ",n)
            break
else:
    print("not a prime number")
    while True:
        n-=1
        b=False
        i=2
        while i<=n//2:
            if n%i==0:
                b=False
                break
            else:
                b=True
                i+=1
        if b==True:
            print("previos prime number = ",n)
            break

