
#     1    
#    212   
#   32123  
#  4321234 
# 543212345

n=int(input("enter the number "))

for i in range(1,n+1):
    a=i
    x=n-i+1
    y=n+i-1
    for j in range(1,2*n):
        if j>=x and j<=y:
            if j<n:
                print(a,end="")
                a-=1
            else:
                print(a,end="")
                a+=1
        else:
            print(" ",end="")

    print()
