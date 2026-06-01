# 6. A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.
# Tasks:
# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0

m=int(input("enter the number of integers "))
n=[]
for i in range(m):
    s=int(input("enter the integers "+str(i+1)+": "))
    n.append(s)

res=[]
pri=[]
for i in n:
    if i not in res:
        res.append(i)
        if i>3:
            for j in range(2,i//2+1):
                if i%j==0:
                    break
            else:
                pri.append(i)
        elif i==2 or i==3:
            pri.append(i)

print(pri)
print("sum =",sum(pri))
print("max =",-1)
print("count =",len(pri))




        



    

