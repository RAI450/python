# ABCDE
#  ABCD
#   ABC
#    AB
#     A

n=int(input("enter the number "))

for i in range(1,n+1):
    a=65
    for j in range(1,n+1):
            if j>=i:
                print(chr(a),end="")
                a+=1
            else:
                print(" ",end="")
    print()