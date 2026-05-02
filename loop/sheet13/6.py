# 6. Composite Number Detector – Risk Version

# A product company marks composite numbers as risky.

# User enters a number.
# System must:

# - Check Composite or Not
# - Count total factors
# - Print smallest factor other than 1

# Input:
# 12

# Output:
# Composite Number
# Factors Count = 6
# Smallest Factor = 2

n=int(input("enter the number "))
count=2                           
a=""
for i in range(2,(n//2)+1):                   #  multi digit factors fails the case because of string
    if n%i==0:
        count+=1
        a=a+str(i)
if count>=3:
    print("composite number")
    print("factors count = ",count)
    for j in a:
        print("smallest factor = ",j )
        break
else:
    print("not a composite number")

    

# n = int(input("enter the number: "))             #  gpt---use of none to print first without loop and break

# count = 0
# smallest = None

# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
        
#         if i > 1 and smallest is None:          #  imp logic
#             smallest = i

# if count > 2:
#     print("Composite Number")
#     print("Factors Count =", count)
#     print("Smallest Factor =", smallest)
# else:
#     print("Not a Composite Number")