# 5. Next Prime ID Generator – Smart Version

# A company gives prime numbered employee IDs to premium staff.

# Manager enters current ID.
# System must:

# - Find next prime number after current ID
# - Find difference between current ID and next prime

# Write a program using loops.

# Input:
# 20

# Output:
# Next Prime ID = 23
# Gap = 3

n=int(input("enter the number "))
cid=n

while True:
    a=True
    n+=1
    for i in range(2,(n//2)+1):
        if n%i==0:
            a=False
            break

    if a==True:
        print("next prime id = ",n)
        break
print("gap = ",n-cid)
