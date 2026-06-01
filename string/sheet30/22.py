n=input("enter the string: ")

for i in n[::-1]:
    count=0
    for j in n:
        if i==j:
            count+=1
        if count>1:
            break
    print(i)
    break
        
