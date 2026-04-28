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

for i in str(num):
    a=int(i)
    fact=1
    for y in range(a,0,-1):
        fact=fact*int(y)
    sum=sum+fact
if sum==num:
    print("strong number")