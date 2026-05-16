# 55555
#  4__4
#   3_3
#    22
#     1

n=int(input("enter the number "))
a=n
for i in range(1,n+1):  
    if i>1 and i<(n-1):
        for j in range(1,n+1):
            if j>i and j<n:
                print("_",end="")
            elif j==i or j==n:
                print(a,end="")
            else:
                print(" ",end="")
        a-=1
        print()
    else:
        for j in range(1,n+1):
            if j>=i:
                print(a,end="")
            else:
                print(" ",end="")
        a-=1
        print()