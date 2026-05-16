#     1
#    10
#   101
#  1010
# 10101

n=int(input("enter the number "))

for i in range(n,0,-1):
    if i%2==0:
        for j in range(1,n+1):
            if j<i:
                print(" ",end="")
            else:
                if j%2==0:
                    print("1",end="")
                else:
                    print("0",end="")
        print()
    
    else:
        for j in range(1,n+1):
            if j<i:
                print(" ",end="")
            else:
                if j%2==0:
                    print("0",end="")
                else:
                    print("1",end="") 
        print()