# 6.
# Palindrome Number Range Checker

# A barcode verification system checks for palindrome numbers within a specific range.
# The user enters starting and ending numbers.
# The system displays all palindrome numbers using nested loops.

# Input:
# Enter starting number: 100
# Enter ending number: 200

# Output:
# Palindrome Numbers are:
# 101
# 111
# 121
# 131
# 141
# 151
# 161
# 171
# 181
# 191

sn=int(input("enter the starting number "))
en=int(input("enter the ending number "))

print("palindrome numbers are:")

for i in range(sn,en+1):
    rev=""
    for j in str(i):
        rev=j+rev
    rev=int(rev)
    if rev==i:
        print(i)

# i=sn
# while i<=en:
#     rev=""
#     j=i
#     while j>0:
#         mod=j%10
#         j=j//10
#         rev=rev+str(mod)
#     if int(rev)==i:
#         print(i)
#     i+=1


