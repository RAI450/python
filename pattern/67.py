#     A    
#    B B   
#   C   C  
#  D     D 
# EEEEEEEEE

n=int(input("enter the number "))

for i in range(1,n+1):
    x=n-i+1
    y=n+i-1
    a=65+i-1
    if i<n:
        for j in range(1,2*n):
            if j==x or j==y:
                print(chr(a),end="")
            else:
                print(" ",end="")
        print()

    else:
        for j in range(1,2*n):
            if j>=x and j<=y:
                print(chr(a),end="")
            else:
                print(" ",end="")
        print()
