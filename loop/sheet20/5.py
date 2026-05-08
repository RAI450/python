# 5. Strong Number Detector

# A banking security system uses Strong Numbers for special authentication testing.
# The user enters a range of numbers.
# The system identifies all Strong Numbers between the given range using nested loops.

# A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

# Example:
# 145

# 1! + 4! + 5!
# = 1 + 24 + 120
# = 145

# Since the sum is equal to the original number, 145 is called a Strong Number.

# Input:
# Enter starting number: 1
# Enter ending number: 500

# Output:
# Strong Numbers are:
# 1
# 2
# 145

sn=int(input("enter the starting number "))
en=int(input("enter the ending number "))

print("strong numbers are:")

# for i in range(sn,en+1):
#     sum=0
#     for j in str(i):
#         pro=1
#         for k in range(int(j),0,-1):
#             pro=pro*k
#         sum=sum+pro
#     if sum==i:
#         print(i)

i=sn
while i<=en:
    sum=0
    j=i
    while j>0:
        mod=j%10
        j=j//10
        pro=1
        k=mod
        while k>0:
            pro=pro*k
            k-=1
        sum=sum+pro
    if sum==i:
        print(i)
    i+=1