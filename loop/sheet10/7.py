# *7. Count Even Digits*
# A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
# Write a program to *count the number of even digits in a given number using loops*.

# Input: 123456
# Output: Even digits count = 3

n=int(input("enter number "))
count=0
while n>0:
    mod=n%10
    if mod%2==0:
        count=count+1
    n=n//10
print("Even digits count = ",count)
