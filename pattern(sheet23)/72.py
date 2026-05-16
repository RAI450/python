

# A B C D E
#  A B C D 
#   A B C  
#    A B   
#     A  

n=int(input("enter the number "))
a=1
b=2*n-1
for i in range(1,n+1):
    x=65
    if i%2==0:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j%2==0:
                    print(chr(x),end="")
                    x+=1
                else:
                    print(" ",end="")
            else:
                print(" ",end="")      
        a+=1
        b-=1
        print()
    else:
        for j in range(1,2*n):
            if j>=a and j<=b:
                if j%2==0:
                    print(" ",end="")
                else:
                    print(chr(x),end="")
                    x+=1
            else:
                print(" ",end="")
        a+=1
        b-=1
        print()