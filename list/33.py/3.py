# 3. Missing Number Detector
# Scenario
# Numbers from 1 to N should exist in a sequence, but one number is missing.

# Requirements

# * Read N and list elements from user
# * Find the missing number
# * Assume numbers belong to the range 1 to N+1

# Test Case 1
# Input:
# [1, 2, 3, 5]

# Output:
# Missing Number = 4

# Test Case 2
# Input:
# [2, 3, 4, 5]

# Output:
# Missing Number = 1

# Test Case 3
# Input:
# [1, 2, 4, 5]

# Output:
# Missing Number = 3

m=int(input("enter the number of user "))
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

a=1
for i in range(len(n)+1):
    if a not in n:
        print("missing number = ",a)
        break
    a+=1
else:
    print("no missing number found")

