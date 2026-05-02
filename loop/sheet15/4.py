# 4.Spy Number Detector

# A cybersecurity system flags special numeric codes.

# A number is called a Spy Number if:
# Sum of digits = Product of digits

# Write a program to check whether the entered number is Spy Number or Not.

# Input:
# 1124

# Output:
# Spy Number

n=int(input("enter the number"))

sum=0
pro=1

for i in str(n):
    sum+=int(i)
    pro=pro*int(i)
if sum==pro:
    print("spy number")
else:
    print("not spy number")