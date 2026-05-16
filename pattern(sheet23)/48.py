#     A
#    AB
#   A_C
#  A__D
# ABCDE


n=int(input("enter the number "))

for i in range(n,0,-1):
    a=65
    if i<=(n-2) and i>1:
        
        for j in range(1,n+1):
            if j<i:
                print(" ",end="")
            elif j>i and j<n:
                print("_",end="")
                a+=1
            else:
                print(chr(a),end="")
                a+=1
        print()
    
    else:
        for j in range(1,n+1):
            if j<i:
                print(" ",end="")
            else:
                print(chr(a),end="")
                a+=1
                  
        print()