#     1
#    12
#   123
#  1234
# 12345

n=int(input("enter the number "))

for i in range(n,0,-1):
    a=1
    for j in range(1,n+1):
        if j<i:
            print(" ",end="")
        else:
            print(a,end="")
            a+=1
    print()
