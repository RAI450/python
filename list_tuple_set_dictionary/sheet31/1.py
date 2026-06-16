# NOTE: in all the programs read length and array elements from user
# =====================================================================
# 1.Student Marks Management
# Create a program to store student marks in a List and perform operations.

# Requirements:

# Add student marks into a List
# Display all marks
# Find highest and lowest marks
# Count students who scored above 75

# Test Cases:

# Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
# Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
# Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3

m=int(input("enter the number of integers "))
n=[]
for i in range(m):
    s=int(input("enter the integers "+str(i+1)+": "))
    n.append(s)

print(n)

hig=0
sml=n[0]
count=0
for i in n:
    if i>hig:
        hig=i
    if i<sml:
        sml=i
    if i>75:
        count+=1
print("highest =",hig)
print("smallest =",sml)
print("count above 75 =",count)
    