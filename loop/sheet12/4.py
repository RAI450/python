# 4. Strong Number Checker

# A digital lock opens only for strong numbers.

# A strong number is a number whose sum of factorial of digits equals the number.

# Example:
# 145 = 1! + 4! + 5!

# Write a program using loops to check strong number.

# Input:
# 145

# Output:
# Strong Number

num=int(input("enter the number "))
a=num
sum=0
while num>0:
    fact=1
    mod=num%10
    for i in range(mod,0,-1):
        fact=fact*i
    sum= sum + fact
    num=num//10
if sum==a:
    print("strong number")
else:
    print("not strong number")




# for i in str(num):                # used for in for
#     a=int(i)
#     fact=1
#     for y in range(a,0,-1):
#         fact=fact*int(y)
#     sum=sum+fact
# if sum==num:
#     print("strong number")