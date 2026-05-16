# *****
# ####
# ***
# ##
# *

n=int(input("enter the number "))

for i in range(n,0,-1):
    if i%2==0:
        for j in range(1,i+1):
            print("#",end="")
        print()
    
    else:
        for j in range(1,i+1):
            print("*",end="")
        print()