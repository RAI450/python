# 1.Second Largest Unique Number
# Scenario

# A sports academy stores athlete scores in a list.

# Find the second largest unique score.

# Requirements
# Read N and list elements from user
# Find second largest unique number
# If not available, display a message
# Test Case

# Input:

# [10, 20, 30, 40, 40]

# Output:

# Second Largest = 30

m=int(input("enter the number of atheletes "))
n=[]

for i in range(m):
    s=int(input("enter the scores for athelete "+str(i+1)+": "))
    n.append(s)

uniq=[]

for i in n:
    if i not in uniq:
        uniq.append(i)

if len(uniq)<2:
    print("not available")
else:
    uniq.sort()
    print("second largest =",uniq[-2])