# 3. Assignment: Prime Number Analyzer using List (Python)

# ## Scenario
# A coaching institute stores student lucky numbers in a Python List.
# Your task is to analyze the list and identify prime numbers for a scholarship selection process.

# You must iterate through every element of the list and perform prime number analysis.

# ---

# # Requirements

# Write a Python program to:

# 1. Store integer values in a List
# 2. Iterate through all elements of the List
# 3. Check whether each number is prime or not
# 4. Display all prime numbers
# 5. Count total prime numbers
# 6. Count total non-prime numbers
# 7. Find the largest prime number from the List
# 8. Store all prime numbers into another List
# 9. Sort the prime numbers in ascending order and display them

# ---

# # Test Case 1

# ## Input

# [2, 3, 4, 5, 6, 7, 8]

# ## Expected Output

# Prime Numbers: 2 3 5 7
# Prime Count: 4
# Non-Prime Count: 3
# Largest Prime Number: 7
# Prime List: [2, 3, 5, 7]
# Sorted Prime List: [2, 3, 5, 7]

# ---

# # Test Case 2

# ## Input

# [10, 11, 12, 13, 14, 15]

# ## Expected Output

# Prime Numbers: 11 13
# Prime Count: 2
# Non-Prime Count: 4
# Largest Prime Number: 13
# Prime List: [11, 13]
# Sorted Prime List: [11, 13]

# ---

# # Test Case 3

# ## Input

# [1, 2, 17, 19, 20, 25]

# ## Expected Output

# Prime Numbers: 2 17 19
# Prime Count: 3
# Non-Prime Count: 3
# Largest Prime Number: 19
# Prime List: [2, 17, 19]
# Sorted Prime List: [2, 17, 19]

# ---

# # Test Case 4

# ## Input

# [4, 6, 8, 9, 10]

# ## Expected Output

# Prime Numbers: None
# Prime Count: 0
# Non-Prime Count: 5
# Largest Prime Number: Not Available
# Prime List: []
# Sorted Prime List: []

# ---

# # Test Case 5

# ## Input

# [29, 31, 37, 41]

# ## Expected Output

# Prime Numbers: 29 31 37 41
# Prime Count: 4
# Non-Prime Count: 0
# Largest Prime Number: 41
# Prime List: [29, 31, 37, 41]
# Sorted Prime List: [29, 31, 37, 41]

m=int(input("enter the number of integers "))
n=[]
for i in range(m):
    s=int(input("enter the integers "+str(i+1)+": "))
    n.append(s)

pri=[]
for i in n:
    if i>3:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            pri.append(i)
    elif i==2 or i==3:
        pri.append(i)
num=" ".join(str(i) for i in pri)   
print("prime numbers: ",num)
print("largest prime number :",max(pri))
print("prime count: ",len(pri))
print("non prime count: ",m-len(pri))
print("prime list: ",pri)
pri.sort()
print("sorted prime list: ",pri)



