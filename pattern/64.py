#     *    
#    *_*   
#   *___*  
#  *_____* 
# *********

n=int(input("enter the number "))

for i in range(1,n+1):
    a=n-i+1
    b=n+i-1
    if i<n:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j==a or j==b:
                    print("*",end="")
                else:
                    print("_",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,2*n):
            print("*",end="")
