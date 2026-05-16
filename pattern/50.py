# 12345
#  1234
#   123
#    12
#     1

n=int(input("enter the number "))

for i in range(1,n+1):
    a=1
    for j in range(1,n+1):
        if j>=i:
            print(a,end="")
            a+=1
        else:
            print(" ",end="")
    print()

