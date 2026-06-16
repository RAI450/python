# 5. Equilibrium Index Finder
# ===========================

# Scenario

# Find an index where:
# # Sum of elements on the left side
# Sum of elements on the right side

# Requirements
# * Read N and list elements from user
# * Find equilibrium index
# * If not found, display message

# Test Case 1
# Input:
# [1, 3, 5, 2, 2]

# Output:
# Equilibrium Index = 2

# Explanation:
# 1 + 3 = 2 + 2

# Test Case 2
# Input:
# [1, 2, 3]

# Output:
# No Equilibrium Index Found

m=int(input("enter the number of user "))
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

for i in range(0,len(n)):
    suml=0
    sumr=0
    for j in range(i):
        suml=suml+n[j]
    for j in range(i+1,len(n)):
        sumr+=n[j]
    if suml==sumr:
        print("equilibrium index = ",i)
        break
else:
    print("no equilibrium index found")



