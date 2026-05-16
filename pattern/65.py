#     1    
#    1 1   
#   1 2 1  
#  1 3 3 1 
# 1 4 4 4 1

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i+1
    y=n+i-1
    if i%2==0:
        for j in range(1,2*n):
            if j>=x and j<=y:
                if j%2==0:
                    if j==x or j==y:
                        print("1",end="")
                    else:
                        print(i-1,end="")
                else:
                    print(" ",end="")
            else:
                print(" ",end="")
        print()

    else:
        for j in range(1,2*n):
            if j>=x and j<=y:
                if j%2==0:
                    print(" ",end="")
                else:
                    if j==x or j==y:
                        print("1",end="")
                    else:
                        print(i-1,end="")
            else:
                print(" ",end="")
        print()

