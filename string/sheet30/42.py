n=input("enter the string: ")
n2=input("enter the string2: ")


l=len(n)
a=len(n2)
if a==l:
    for i in range(l):
        if n[i]!=n2[i]:
            print("not equal")
            break
    else:
        print("equal")
else:
    print("not equal")

        