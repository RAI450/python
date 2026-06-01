n=input("enter the string: ")
n2=input("enter the string2: ")

l=len(n)
b=len(n2)
res=list(n)
if l==b:
    for j in range(l):
        a=[]
        for i in range(l):
            if i==(l-1):
                a[i]=res[0]
            else:
                a[i]=res[i+1]
        res=a
        a=a.join()

        if a==n2:
            print("it is the left form")
            break