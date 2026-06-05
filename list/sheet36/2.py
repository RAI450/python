# 2.
# Secure Password Analysis

# A cybersecurity team wants to identify pairs of passwords having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 3

# Explanation

# ("abc","de")
# ("abc","fg")
# ("de","fg")

n= int(input("enter the number of strings : "))

pswrd=[]
for i in range(n):
    d=input("enter the strings : ")
    pswrd.append(d)
print(pswrd)

row=[]
for i in range(n):
    res=""
    for j in pswrd[i]:
        res+=j
    for k in range(i+1,n):
        for l in pswrd[k]:
            if l in res:
                break
        else:
            d=[pswrd[i],pswrd[k]]
            row.append(d)
    

for i in row:
    print(f"({i[0]},{i[1]})")
