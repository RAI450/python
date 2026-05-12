# 15) Zig-Zag Star
#     *   *   *
#       *   *
#     *   *   *

n=int(input("enter the number "))

for i in range(1,n+1):
    if i%2==0:
        for j in range(1,2*n):
            if j%2==0:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,(2*n)+1):
            if j%2==0:
                print(" ",end="")
            else:
                print("*",end="")
        print()


            
        