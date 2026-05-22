# 4.

# Find All Characters with Maximum Frequency
# Website Traffic Analysis System

# A web analytics company tracks user activity symbols in server logs.

# The company wants to identify all characters having the maximum frequency in the given string.

# Input:
# aabbbccddd
# Output:
# b d

n=input("enter the string: ")

res=""
hig=0
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count>hig:
        hig=count
        res=i+" "
    elif count==hig and i not in res:
        res=res+i
print(res)


