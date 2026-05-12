# 2) Hollow Rectangle
#     ***
#     *       *
#     *       *
#     *       *
#     ***

n=int(input("enter the number "))

for i in range(1,n+1):
    if i==1 or i==n:
        for j in range(1,n+1):
            if j>1 and j<n:
                print("*",end="")
            else:
                print(" ",end="")
        print()

    else:
        for j in range(1,n+1):
            if j==1 or j==n:
                print("*",end="")
            else:
                print(" ",end="")
        print()