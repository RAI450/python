# 23) Plus Star Pattern
#           *
#           *
#     ***
#           *
#           *

n=int(input("enter the number "))

for i in range(1,2*n):
    if i==n:
        for j in range(1,2*n):
            print("*",end="")
        print()
    else:
        for j in range(1,n+1):
            if j==n:
                print("*",end="")
            else:
                print(" ",end="")
        print()
                