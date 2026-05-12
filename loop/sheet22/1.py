# 1) Hollow Pyramid
#         *
#        * *
#       *   *
#      *     *
#     ***

n= int(input("enter the number "))

for i in range(1,n+1):
    if i<n:
        nxt=n+i-1
        prev=n-i+1
        for j in range(1,2*n):
            if j==nxt or j==prev:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,2*n):
            print("*",end="")