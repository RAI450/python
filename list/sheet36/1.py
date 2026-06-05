# 1. Count Pairs with Difference K

# A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

# Problem Statement:

# Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

# Example:

# Input:

# N = 5
# K = 2
# ages[] = {1, 5, 3, 4, 2}

# Output:

# 3

# Explanation:

# (1,3), (3,5), (2,4)

n= int(input("enter the number of employees : "))
k=int(input("enter the absolute difference :"))

age=[]
for i in range(n):
    d=int(input("enter the ages"))
    age.append(d)
print(age)

res=[]
for i in range(n):
    row=[]
    for j in range(i+1,n):
        if abs(age[i]-age[j])==k:
            row=[age[i],age[j]]
            res.append(row)

for i in res:
    print(f"({i[0]},{i[1]})", end=", ")



