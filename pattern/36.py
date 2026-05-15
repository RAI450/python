# ABCDE
# A  D
# A C
# AB
# A

n=int(input("enter the number "))

for i in range(n,0,-1):
    a=65
    if i==n:
        for j in range(1,i+1):
            print(chr(a),end="")
            a+=1
        print()
    else:
        for j in range(1,i+1):
            if j==1 or j==i:
                print(chr(a),end="")
                a+=1
            else:
                print(" ",end="")
                a+=1
        print()