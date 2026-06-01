# 2.Smart City Traffic Peak Load Analyzer

# Problem Statement
# A smart city monitors traffic density at different time intervals in a day.
# An element is called a peak traffic point if it is greater than or equal to its adjacent elements.
# You are given an array traffic[] of size N.

# Tasks:

# Find all peak elements
# Calculate the sum of all peak traffic values
# Find the product of all peak traffic values
# Return the maximum peak value

# Note:
# If only one element exists, it is the only peak.

# Test Case 1

# Input:
# traffic = [10, 50, 30, 70, 60, 90, 80]

# Output:
# Peaks = [50, 70, 90]
# Sum = 210
# Product = 315000
# Max Peak = 90

# Test Case 2

# Input:
# traffic = [100, 200, 150, 180, 170]

# Output:
# Peaks = [200, 180]
# Sum = 380
# Product = 36000
# Max Peak = 200

# Test Case 3

# Input:
# traffic = [5]

# Output:
# Peaks = [5]
# Sum = 5
# Product = 5
# Max Peak = 5

m=int(input("enter the number of points "))
n=[]

for i in range(m):
    s=int(input("enter the checkpoint "+str(i+1)+": "))
    n.append(s)

pek=[]

if len(n)>1:

    for i in range(len(n)):
        if i==0:
            if n[i]>n[i+1]:
                pek.append(n[i])
        elif i==len(n)-1:
            if n[i]>n[i-1]:
                pek.append(n[i])
        else:
            if n[i]>n[i+1] and n[i]>n[i-1]:
                pek.append(n[i])
    sum=0
    pro=1
    for i in pek:
        sum=sum+i
        pro=pro*i
    if len(pek)==0:
        print("no peak checkpoint found")
    else:
        print("peaks =",pek)
        print("sum =",sum)
        print("product =",pro)
        print("max peak = ",max(pek))

else:
    print(n[0])