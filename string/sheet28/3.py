# 3.Replace Consecutive Duplicate Characters with Single Character
# Data Compression System

# A cloud storage company wants to reduce unnecessary repeated characters in text logs.

# Write a Python program that replaces consecutive duplicate characters with a single occurrence.

# Input:
# aaabbbccccdddaa
# Output:
# abcda

n=input("enter the string: ")

l=len(n)
res=n[0]
for i in range(1,l):
    if n[i]!=n[i-1]:
        res=res+n[i]
print(res)



# for i in n:
#     for j in range(l):
#         if n[j-1]!=i:
#             res=res+i
        



    



