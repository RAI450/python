# 19) Reverse Number Cross
#     5   5
#      4 4
#       3
#      4 4
#     5   5

n=int(input("enter the number "))
y=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==y:
            if i<=(n//2)+1:
                print(y,end="")
            else:
                print(i,end="")          
        else:
            print(" ",end="")
    print()
    y-=1