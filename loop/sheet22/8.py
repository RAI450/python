# 8) Border Number Pattern
#     1 2 3 4 5
#     2       5
#     3       5
#     4       5
#     5 5 5 5 5

n=int(input("enter the number "))

for i in range(1,n+1):
    if i<=(n-1):
        for j in range(1,n+1):
            if i==1:
                print(j,end=" ")
            else:
                if j==1:
                    print(i,end=" ")
                elif j==n:
                    print("5",end=" ")
                else:
                    print(" ",end=" ")
        print()

    else:
        for j in range(1,n+1):
            print("5",end=" ")
