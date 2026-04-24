# *11. Count Occurrence of a Digit*
# A system logs repeated digits in a number for pattern analysis and reporting.
# Write a program to *count how many times a given digit appears in a number using loops*.

# Input: Number = 122312, Digit = 2
# Output: 3

n=int(input("enter number "))
dig=int(input("enter digit "))

rep=0
while n>0:
    mod=n%10
    if mod==dig:
        rep=rep+1
    n=n//10
print(rep)