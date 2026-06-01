n=input("enter the string: ")

s=n.split()
res=""
hig=0
for i in s:
    count=0
    for j in i:
        count+=1
    if count>hig:
        hig=count
        res=i
print(res)