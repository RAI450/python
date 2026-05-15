# ABCDE
# ABCD
# ABC
# AB
# A

n=int(input("enter the number "))

for i in range(n,0,-1):
    a=65
    for j in range(1,i+1):
        print(chr(a),end="")
        a+=1
    print()