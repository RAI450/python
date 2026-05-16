
# 11111
#  2222
#   333
#    44
#     5
n=int(input("enter the number "))
a=1
for i in range(1,n+1):
    for j in range(1,n+1):
            if j>=i:
                print(a,end="")
                
            else:
                print(" ",end="")
    a+=1
    print()