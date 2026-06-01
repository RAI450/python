n=input("enter the string: ")
char=input("enter the character: ")

res=""
l=len(n)
for i in range(l):
    if n[i]==char:
        res=res+str(i)+" "
print(res)