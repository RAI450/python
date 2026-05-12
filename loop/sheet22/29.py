# 29) Diagonal Number Square
#     1 - - -
#     - 2 - -
#     - - 3 -
#     - - - 4

n=int(input("enter the number "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i:
            print(j,end=" ")
        else:
            print("-",end=" ")
    print()