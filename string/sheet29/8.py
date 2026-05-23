# # 8. Intelligent Search Query Compressor

# A search engine company wants to compress user queries.

# ## Rules:

# * Count frequency of each character
# * Display characters in sorted order
# * Ignore spaces
# * Case insensitive

# ### Input:
# text
# Google Search

# ### Output:
# text
# a1c1e2g2h1l1o2r1s1

n=input("enter the string: ").lower()

res=""
n=sorted(n)
for i in n:
    count=0
    if i!=" " and i not in res:
        for j in n:
            if i==j:
                count+=1
        res+=i+str(count)
print(res)





