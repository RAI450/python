# 7.Neon Number Detector

# Scenario:
# A smart calculator system checks special numbers used in mathematical testing.
# The user enters a range of numbers.
# The system identifies all Neon Numbers using nested loops.

# Theory:
# A Neon Number is a number where the sum of digits of its square is equal to the original number.

# Example:
# 9

# Square of 9 = 81

# 8 + 1 = 9

# Since the sum is equal to the original number, 9 is called a Neon Number.

# Input:
# Enter starting number: 1
# Enter ending number: 100

# Output:
# Neon Numbers are:
# 1
# 9

sn=int(input("enter the starting number "))
en=int(input("enter the ending number "))

print("neon numbers are:")

for i in range(sn,en+1):
    sqr=i**2
    sum=0
    for j in str(sqr):
        sum+=int(j)
    if sum==i:
        print(i)

# i=sn
# while i<=en:
#     sqr=i**2
#     sum=0
#     j=sqr
#     while j>0:
#         mod=j%10
#         j=j//10
#         sum+=mod
#     if sum==i:
#         print(i)
#     i+=1

