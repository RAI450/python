n=input("enter the word:")

hig=0
res=""
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count>hig:
        hig=count
        res=i
print(res)