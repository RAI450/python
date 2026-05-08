# 3.
# Prime Number Range Checker

# A cyber security system generates prime numbers for encryption analysis.
# The user enters a starting number and ending number.
# The system checks and displays all prime numbers between the given range using nested loops.

# Input:
# Enter starting number: 10
# Enter ending number: 50

# Output:
# Prime Numbers are:
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47

sn=int(input("enter the starting number "))
en=int(input("enter the ending number "))

print("prime numbers are:")
# for i in range(sn,en+1):
#     if i>1:
#         for j in range(2,(i//2)+1):
#             if i%j==0:
#                 break
#         else:
#             print(i)

i=sn
while i<=en:
    if i>1:
        j=2
        while j<=(i//2):
            if i%j==0:
                break
            j+=1
        else:
            print(i)
    i+=1
            


