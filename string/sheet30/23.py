n=input("enter the string: ")

res=""
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count==2 and i not in res:
        res+=i+" "
print(res)