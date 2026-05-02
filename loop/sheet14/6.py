# 6.Next Prime Cabin Number Generator

# A luxury hotel gives only prime numbered cabins to VIP guests.

# Manager enters the last allotted cabin number.
# System must find the next available prime cabin number.

# Write a program using loops.

# Input:
# 24

# Output:
# Next Prime Cabin = 29

n=int(input("enter the number "))

x=True
while True:   
    n+=1  
    print(n)                     
    for i in range(2,(n//2)+1):                   ##  NOT DONE
        if n%i==0:
            x=False
            break
        else:
            x=True
    break
if x==True:
    print(n)
    
    

