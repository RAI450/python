# 8. Number Property Checker
#    A system evaluates number properties:

# * If number % 2 == 0 → Even number
# * If number % 5 == 0 → Divisible by 5

# Input:
# Enter number: 20

# Output:
# Even number
# Divisible by 5


num=int(input("enter the number"))

if num%2==0:
    print("even number")

if num%5==0:
    print("divisible by 5")