# 5.Number Stability Analyzer

# A science lab studies whether digits are in increasing order.

# Write a program using for-else loop:

# - If every next digit is greater than previous print Stable Number
# - Else Unstable Number

# Input:
# 12359

# Output:
# Stable Number

n=int(input("enter the number "))

a=0
for i in str(n):
    if int(i)>=a:
        a=int(i)
    else:
        print("unstable number")
        break
else:
    print("stable number")






# a=0                                   # using without for else loop
# x=True
# for i in str(n):
#     if int(i)>=a:
#         a=int(i)
#     else:
#         x=False
#         break
# if x==True:
#     print("stable number")
# else:
#     print("unstable number")
