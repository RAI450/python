#     1
#    11
#   1*1
#  1**1
# 11111

n=int(input("enter the number "))

for i in range(n,0,-1):
    if i<=(n-2) and i>1:
        for j in range(1,n+1):
            if j<i:
                print(" ",end="")
            elif j>i and j<n:
                print("*",end="")
            else:
                print("1",end="")
        print()
    
    else:
        for j in range(1,n+1):
            if j<i:
                print(" ",end="")
            else:
                print("1",end="")
                  
        print()