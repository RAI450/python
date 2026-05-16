
#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1

n=int(input("enter the number "))

for i in range(1,2*n):
    if i==n:
        for j in range(1,2*n):
            if j<=n:
                print(j,end="")
            else:
                print((2*n)-j,end="")
        print()
    elif i<n:
        for j in range(1,n+1):
            if j==n:
                print(i,end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,n+1):
            if j==n:
                print((2*n)-i,end="")
            else:
                print(" ",end="")
        print()



