s=input("enter the word: ")
r=input("enter the character: ")

res=""
for i in s:
    if i!=r:
        res+=i

print(res)