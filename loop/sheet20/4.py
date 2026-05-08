# 4.Armstrong Number Finder

# A digital number analysis system checks for Armstrong numbers within a range.
# The user enters starting and ending numbers.
# The system finds all Armstrong numbers using nested loops.

# Input:
# Enter starting number: 1
# Enter ending number: 500

# Output:
# Armstrong Numbers are:
# 1         # 2,3,4,5,6,,8,9
# 153
# 370
# 371
# 407

sn=int(input("enter the starting number "))
en=int(input("enter the ending number "))

print("armstrong numbers are:")

for i in range(sn,en+1):
    l=len(str(i))
    pro=0
    for j in str(i):
        pro=pro+(int(j)**l)
    if pro==i:
        print(i)

# i=sn                          #    by while
# while i<=en:
#     l=len(str(i))
#     pro=0
#     j=i
#     while j>0:
#         mod=j%10
#         j=j//10
#         pro=pro+(mod**l)
#     if pro==i:
#         print(i)
#     i+=1



    