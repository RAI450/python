# 4. Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.

A =[1,5,10, 20, 40, 80]
B =[6, 7, 20, 80, 100]
C =[3, 4, 15, 20, 30, 70, 80, 120]

max=None
if len(A)>len(B) and len(A)>len(C):
    max=A
elif len(B)>len(C):
    max=B
else:
    max=C

res=""
for i in max:
    if i in A and i in B and i in C:
        res+=str(i)+" "
print(res)



