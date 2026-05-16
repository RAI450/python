#     x    
#    x_x   
#   x___x  
#  x_____x 
# xxxxxxxxx

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i+1
    y=n+i-1
    if i<n:
        for j in range(1,2*n):
            if j>=x and j<=y:
                if j==x or j==y:
                    print("x",end="")
                else:
                    print("_",end="")
            else:
                print(" ",end="")
        print()
    
    else:
        for j in range(1,2*n):
            print("x",end="")
