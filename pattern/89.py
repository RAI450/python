
#      1     
#     101    
#    10101   
#   1010101  
#  101010101 
# 10101010101

n=int(input("enter the number "))
if n%2==0:
    for i in range(1,n+1):
        x=n-i+1
        y=n+i-1
        if i%2==0:
            for j in range(1,2*n):
                if j>=x and j<=y:
                    if j%2==0:
                        print("0",end="")
                    else:
                        print("1",end="")
                else:
                    print(" ",end="")
            print()
        else:
            for j in range(1,2*n):
                if j>=x and j<=y:
                    if j%2==0:
                        print("1",end="")
                    else:
                        print("0",end="")
                else:
                    print(" ",end="")
            print()
else:
    for i in range(1,n+1):
        x=n-i+1
        y=n+i-1
        if i%2==0:
            for j in range(1,2*n):
                if j>=x and j<=y:
                    if j%2==0:
                        print("1",end="")
                    else:
                        print("0",end="")
                else:
                    print(" ",end="")
            print()
        else:
            for j in range(1,2*n):
                if j>=x and j<=y:
                    if j%2==0:
                        print("0",end="")
                    else:
                        print("1",end="")
                else:
                    print(" ",end="")
            print()
