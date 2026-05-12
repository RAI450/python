# 22) Inverted Hollow Pyramid
#     ***
#      *     *
#       *   *
#        * *
#         *

n= int(input("enter the number "))

for i in range(1,n+1):
    if i>1:
        nxt=2*n-i
        prev=i
        for j in range(1,2*n):
            if j==nxt or j==prev:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,2*n):
            print("*",end="")
        print()
