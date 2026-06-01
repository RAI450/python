# 2.Student Pass List Generator (Using List Comprehension)

# A school stores student marks in a list. Generate a new list containing only the marks of students who have passed (marks ≥ 40).

# Requirements
# Read N and marks from user
# Use List Comprehension
# Create Pass List
# Display Pass Count
# Test Case

# Input:

# [25, 40, 55, 78, 30, 90]

# Output:

# Pass List = [40, 55, 78, 90]
# Pass Count = 4

m=int(input("enter the number of students "))
n=[]

for i in range(m):
    s=int(input("enter the marks for stu."+str(i+1)+": "))
    n.append(s)

#  using list comprehension-------------

pas=[i  for i in n if i>=40]
print("pass list ",pas)
print("pass count =",len(pas))

# simple method------------------------

# pas=[]
# count=0
# for i in n:
#     if i>=40:
#         pas.append(i)
#         count+=1

# print("pass list ",pas)
# print("pass count =",count)
