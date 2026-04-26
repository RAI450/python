# 10. Student ID Validity Checker (Count Odd Digits)
# A school management system assigns numeric IDs to students. 
# The administration wants to verify IDs by checking how many odd digits are present in each ID number. 
# IDs with more odd digits are sent for manual review.

# Write a program to count the number of odd digits in a given student ID using loops.

# Input:
# 572943

# Output:
# Odd Digits Count = 3

num=int(input("enter the number "))

count=0
for i in str(num):
    if int(i)%2!=0:
        count+=1
print("odd digits count = ",count)