# 6.Product Code Verification System

# An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

# Conditions:
# - Ignore spaces
# - Ignore case sensitivity

# Input:
# Enter first product code: Dormitory
# Enter second product code: Dirty Room

# Output:
# Both Product Codes are Matching

n=input("Enter first product code: ")
n2=input("Enter second product code: ")

nw=""
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        nw=nw+chr(ord(i)+32)
    elif i==" ":
        continue
    else:
        nw+=i

nw2=""
for i in n2:
    if ord(i)>=65 and ord(i)<=90:
        nw2=nw2+chr(ord(i)+32)
    elif i==" ":
        continue
    else:
        nw2+=i

flag=1
for i in nw:
    countn=0
    countn2=0
    for j in nw:
        if j==i:
            countn+=1
    for k in nw2:
        if k==i:
            countn2+=1
    if countn!=countn2:
        flag=0
        break

if flag==0:
    print("both product code are not matching")
else:
    print("both product code are  matching")