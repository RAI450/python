#     A    
#    A B   
#   A B C  
#  A B C D 
# A B C D E

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i+1
    y=n+i-1
    a=65
    if i%2==0:
        for j in range(1,2*n):
            if j>=x and j<=y:
                if j%2==0:
                    print(chr(a),end="")
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
                    print(chr(a),end="")
                    a+=1
            else:
                print(" ",end="")
        print()