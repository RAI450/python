# 3. First Digit of Number
# A university receives thousands of application IDs. 
# The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
# Write a program to find the first digit of a number using loops.

# Input:
# 53892

# Output:
# First Digit = 5
num=input("enter the number")


for i in num:                        # using break
    print("first digit = ",i)
    break


# a=True                               # unnecessary many times loop is working
# for i in num:
#     count=count+1
#     if a==True:
#         print("first digit = ",i)
#         a=False
