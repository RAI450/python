# 7. Array Rotation Analyzer
# Scenario
# Rotate the array K times towards the right.

# Requirements
# * Read N and list elements from user
# * Read K
# * Rotate the array
# * Display rotated array

# Test Case 1
# Input:
# Array = [1, 2, 3, 4, 5]
# K = 2

# Output:
# [4, 5, 1, 2, 3]

# Test Case 2
# Input:
# Array = [10, 20, 30, 40]
# K = 1

# Output:
# [40, 10, 20, 30]

m=int(input("enter the number of user "))               
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

t=int(input("enter the number of times to rotate"))
new=[]
j=1
while j<=t:
    for i in range(len(n)):
        if i==0:
            new.append(n[len(n)-1])
        else:
            new.append(n[i-1])
    n=new
    new=[]
    j+=1
print(n)

# one logic if lenght in n then after every nth rotain it gives original string