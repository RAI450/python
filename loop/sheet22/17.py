# 17) Hollow Hourglass
#     * * * * *
#       *     *
#         * *
#           *
#         * *
#       *     *
#     * * * * *

n=int(input("enter the number"))
for i in range(1,n+1):
    if i<=(n//2)+1:
        x=i
        y=(n-i)+1
        if i==1:
            for j in range(1,n+1):
                if j%2==0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()
        else:
            for j in range(1,n+1):
                if j==x or j==y:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    else:
        y=(n-i)+1
        if i==n:
            for j in range(1,n+1):
                if j%2==0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()
        else:
            for j in range(1,n+1):
                if j==i or j==y:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()




