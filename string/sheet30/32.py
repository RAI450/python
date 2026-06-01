n=input("enter the string: ")

s=n.split()
res=""
for i in s:
    count=0
    if i not in res:
        res+=i+" "
        for j in s:
            if i==j:
                count+=1
        print(i,"= ",count)
