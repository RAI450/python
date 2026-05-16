# ABCDE
#  A__C
#   A_B
#    AB
#     A

n=int(input("enter the number "))

for i in range(1,n+1):
    a=65
    if i>1 and i<(n-1):
        for j in range(1,n+1):
            if j>i and j<n:
                print("_",end="")
                a+=1
            elif j==i or j==n:
                print(chr(a),end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(1,n+1):
            if j>=i:
                print(chr(a),end="")
                a+=1
            else:
                print(" ",end="")
        print()