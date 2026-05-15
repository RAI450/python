# a
# bc
# def
# ghij
# klmno


n=int(input("enter the number "))

a=97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(a),end=" ")
        a+=1
    print()