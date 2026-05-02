# 8.
# Trimorphic Number Analyzer

# A coding system checks cube-based patterns.

# A Trimorphic Number:
# Cube of number ends with the same number.

# Example:
# 4³ = 64

# Write a program to check Trimorphic Number.

# Input:
# 4

# Output:
# Trimorphic Number

n=int(input("enter the number"))

n3=n**3
for i in str(n):
    if n%10!=n3%10:
        print("not a trimorphic number")
        break
    n=n//10
    n3=n3//10
else:
    print("trimorphic number")