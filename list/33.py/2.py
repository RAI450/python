# 2. First Repeating Number
# =========================

# Scenario

# A security system logs employee IDs.

# Find the first ID that repeats in the list.

# Requirements

# * Read N and list elements from user
# * Find the first repeating number
# * If no repeating number exists, display an appropriate message

# Test Case 1

# Input:
# [10, 5, 3, 4, 3, 5]

# Output:
# First Repeating Number = 5

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Repeating Number Found

m=int(input("enter the number of user "))
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count>1:
        print("first repeating number :",i)
        break
else:
    print("no repeating number found")
    

