# A
# AB
# A C
# A  D
# ABCDE


n=int(input("enter the number "))

for i in range(1,n+1):
    if i<=n-1:
        a=65
        for j in range(1,i+1):
            if j==1 or j==i:
                print(chr(a),end="")
            else:
                print(" ",end="")
            a=a+1
        print()
    else:
        a=65
        for j in range(1,n+1):
            print(chr(a),end="")
            a+=1