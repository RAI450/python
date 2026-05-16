#     1    
#    1 2   
#   1 2 3  
#  1 2 3 4 
# 1 2 3 4 5

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i+1
    y=n+i-1
    a=1
    if i%2==0:
        for j in range(1,2*n):
            if j>=x and j<=y:
                if j%2==0:
                    print(a,end="")
                    a+=1
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
                    print(a,end="")
                    a+=1
            else:
                print(" ",end="")
        print()