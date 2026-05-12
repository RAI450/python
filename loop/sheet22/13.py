# 13) Number X Pattern
#     1   5
#      2 4
#       3
#      2 4
#     1   5

n=int(input("enter the number "))
y=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==y:
            print(j,end="")
        else:
            print(" ",end="")
    print()
    y-=1

