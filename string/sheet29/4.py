# # 4. Cloud Storage Duplicate File Name Resolver

# A cloud storage company stores uploaded filenames from users.

# Sometimes multiple duplicate filenames are uploaded.

# The system should:

# * Keep the first occurrence unchanged
# * Add (1), (2), (3)... for duplicates

# ### Input:

# text
# file file image file image data


# ### Output:

# text
# file file(1) image file(2) image(1) data


n=input("enter the sentence: ")

s=n.split()
res=""
a=1
l=len(s)
for i in s:
    count=0
    for j in range(a,l):
        if i==s[j]:
            count+=1
            s[j]=s[j]+"("+str(count)+")"
    a+=1
print(" ".join(s))
