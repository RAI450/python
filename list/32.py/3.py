# 3.Industrial Sensor Peak Energy Monitoring System

# Problem Statement
# A factory machine records energy consumption at regular intervals.
# A peak is defined as a value greater than or equal to its neighbors.

# Tasks:
# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# If no peaks, return -1

# Test Case 1
# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2
# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1925
# Average = 25
# Difference = 10

# Test Case 3
# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0

m=int(input("enter the number of records "))
n=[]

for i in range(m):
    s=int(input("enter the records "+str(i+1)+": "))
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
    pro=0
    for i in pek:
        sum=sum+i
        pro=pro+i**2
    if len(pek)==0:
        print("-1")
    else:
        print("peaks =",pek)
        print("sum of squares =",pro)
        print("average = ",sum/len(pek))
        print("difference = ",max(pek)-min(pek))

else:
    print(n[0])