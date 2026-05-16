# 5 5 5 5 5
#  4 4 4 4 
#   3 3 3  
#    2 2   
#     1   

n=int(input("enter the number "))
a=1
b=2*n-1
x=5
for i in range(1,n+1):
    if i%2==0:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j%2==0:
                    print(x,end="")
                else:
                    print(" ",end="")
            else:
                print(" ",end="")      
        a+=1
        b-=1
        x-=1
        print()
    else:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j%2==0:
                    print(" ",end="")
                else:
                    print(x,end="")
    
            else:
                print(" ",end="")
        a+=1
        b-=1
        x-=1
        print()