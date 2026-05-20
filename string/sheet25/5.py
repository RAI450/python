# 5.
# Palindrome Product Code Checker

# A factory wants to identify whether a product code reads the same forward and backward.

# Input:
# Enter product code: MADAM

# Output:
# Palindrome Code

# Input:
# Enter product code: PRODUCT

# Output:
# Not a Palindrome Code

n=input("Enter product code: ")

rev=""
for i in n:
    rev=i+rev

if n==rev:
    print("palindrome code")
else:
    print("not a palindrome code")

