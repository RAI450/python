# 6. Product Except Self
# Scenario
# For every element, calculate the product of all other elements except itself.

# Requirements
# * Read N and list elements from user
# * Create a new list containing products
# * Display the result

# Test Case 1
# Input:
# [1, 2, 3, 4]

# Output:
# [24, 12, 8, 6]

# Test Case 2
# Input:
# [2, 3, 5]

# Output:
# [15, 10, 6]

m=int(input("enter the number of user "))
n=[]

for i in range(m):
    s=int(input("enter the number "+str(i+1)+": "))
    n.append(s)

pro=[]

for i in range(len(n)):
    prod=1
    for j in range(len(n)):
        if i==j:
            continue
        else:
            prod=prod*n[j]
    pro.append(prod)
print(pro)


