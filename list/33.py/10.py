# 10. Find Duplicate Numbers
# Scenario

# A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

# Requirements

# * Read N and list elements from user
# * Find all duplicate numbers
# * Store duplicates in another list
# * Count total duplicate numbers
# * Display duplicates in sorted order

# Test Case 1

# Input:
# [1, 2, 3, 2, 4, 5, 1]

# Output:
# Duplicate Numbers = [1, 2]
# Count = 2

# Test Case 2

# Input:
# [10, 20, 30]

# Output:
# No Duplicate Numbers Found

m=int(input("enter the number of user "))               
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

dup=[]
res=[]
for i in n:
    count=0
    if i not in res:
        res.append(i)
        for j in n:
            if i==j:
                count+=1
                if count>1:
                    dup.append(j)
if len(dup)>=1:
    dup.sort()
    print("duplicate numbers = ",dup)
    print("count =",len(dup))
else:
    print("no duplicate numbers found")



