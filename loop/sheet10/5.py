# 5. Palindrome Check
# A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
# Write a program to *check whether a given number is a palindrome using loops*.

# Input: 121
# Output: Palindrome

ori=int(input("enter number "))
n=ori
rev=0
i=0
while n>0:
    mod=n%10
    n=n//10
    rev=(rev*10)+mod
    i=i+1

if ori==rev:
    print("palindrome")
else:
    print("not palindrome")