# 2. Next Prime ID Generator

# A multinational company auto-generates employee IDs in numeric sequence.
#  Due to internal policy, only prime numbered IDs are assigned to new premium employees.

# The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

# Write a program to find the first prime number after n.

# Input:
# 14

# Output:
# Next Prime = 17

num=int(input("enter number "))
a=False                                 #use of while in while
while True:
    num=num+1
    i=2
    while i<=num//2:
        if num%i==0:
            a=False
            break
        else:
            a=True
            i+=1
    if a==True:
        print(num)
        break

