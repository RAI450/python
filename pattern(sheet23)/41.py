# A
# BCD
# EFGHI
# JKLMNOP

n=int(input("enter the number "))

a=65
for i in range(1,n+1):
    for j in range(1,2*i):
        print(chr(a),end="")
        a+=1
    print()