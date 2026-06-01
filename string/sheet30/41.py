n=input("enter the string: ")
char=input("enter the character: ")

l=len(n)
lc=len(char)

for i in range(l):
    if n[i]==char[0]:
        for j in range(lc):
            if n[i+j]!=char[j]:
                break
        else:
            print("true")
            break
