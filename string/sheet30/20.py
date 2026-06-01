n=input("enter the word:")

sml=9
res=""
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count<=sml:
        sml=count
        res=res+i
        
print(res)