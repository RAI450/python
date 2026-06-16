# 4. Longest Consecutive Sequence
# Scenario
# Find the longest sequence of consecutive numbers present in the list.

# Requirements
# * Read N and list elements from user
# * Find the length of the longest consecutive sequence
# * Display the sequence length

# Test Case 1
# Input:
# [100, 4, 200, 1, 3, 2]

# Output:
# Longest Consecutive Length = 4

# Explanation:
# Sequence = 1, 2, 3, 4

# Test Case 2
# Input:
# [10, 11, 12, 20]

# Output:
# Longest Consecutive Length = 3

m=int(input("enter the number of user "))
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

max=0
for i in n:
    a=i
    count=1
    for j in n:
        if a+1 in n:
            count+=1
            a=a+1
        else:
            break
    if count>max:
        max=count

print("Longest Consecutive Length = ",max)

