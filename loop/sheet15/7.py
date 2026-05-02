# 7.Adam Number Verification System – Question

# A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

# When a user enters a numeric code, the system performs a dual verification process:

# * It calculates the square of the entered number.
# * It reverses the number and calculates the square of the reversed value.
# * Finally, it checks whether both results are mirror images (reverses) of each other.

# A number is called an Adam Number if:
# The square of the number and the square of its reverse are reverses of each other.

# Task:
# Write a Python program to check whether a given number is an Adam Number or not.

# Examples:

# Input:
# 12
# Output:
# Adam Number

# Input:
# 13
# Output:
# Not an Adam Number      # wrong it is a adam number

# Input:
# 11
# Output:
# Adam Number

# Example:
# 12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144

n=int(input("enter the number"))

n2=n**2
rev=""

while n>0:
    rev+=str(n%10)
    n=n//10
rev=int(rev)
rev2=rev**2

x=True
for i in str(rev2):
    if int(i)!=(n2%10):
        x=False
        break
    else:
        n2=n2//10

if x==True:
    print("adam number")
else:
    print("not an adam number")

        

