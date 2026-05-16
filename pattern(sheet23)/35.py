# *****
# *  *
# * *
# **
# *

n=int(input("enter the number "))

for i in range(n,0,-1):
    if i==n:
        for j in range(1,i+1):
            print("*",end="")
        print()
    else:
        for j in range(1,i+1):
            if j==1 or j==i:
                print("*",end="")
            else:
                print(" ",end="")
        print()