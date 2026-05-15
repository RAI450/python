# EEEEE
# DDDD
# CCC
# BB
# A

n=int(input("enter the number "))

for i in range(n,0,-1):
    a=65+i-1
    for j in range(1,i+1):
        print(chr(a),end="")
    print()