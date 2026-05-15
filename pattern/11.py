# A
# AB
# ABC
# ABCD
# ABCDE

n=int(input("enter the number "))

for i in range(1,n+1):
    a=65
    for j in range(1,i+1):
        print(chr(a),end="")
        a+=1
    print()