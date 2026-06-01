# 8. Majority Element Detector
# Scenario

# Find an element occurring more than N/2 times.

# Requirements

# * Read N and list elements from user
# * Find majority element
# * If not present, display appropriate message

# Test Case 1

# Input:
# [2, 2, 1, 2, 3, 2, 2]

# Output:
# Majority Element = 2

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Majority Element Found

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
    if count>len(n)//2:
        print("majority element = ",i)
        break
else:
    print("no majority element found")


