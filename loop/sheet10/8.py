# *8. Count Odd Digits*
# A banking system flags IDs with too many odd digits for further verification.
# Write a program to *count the number of odd digits in a given number using loops*.

# Input: 123456
# Output: Odd digits count = 3

n=int(input("enter number "))
count=0
while n>0:
    mod=n%10
    if mod%2!=0:
        count=count+1
    n=n//10
print("odd digits count = ",count)