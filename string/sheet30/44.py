n=input("enter the string: ")
n2=input("enter the string2: ")

if len(n)==len(n2):
    for i in n:
        if n.count(i)!=n2.count(i):
            print("not a anagrams")
            break
    else:
        print("anagram")
else:
    print("not a anagrams")

