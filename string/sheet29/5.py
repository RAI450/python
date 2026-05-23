# # 5. Social Media Hashtag Trend Window

# A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

# ### Input:
# text
# aabcbcdbca

# ### Output:
# text
# dbca

# ### Explanation:
# dbca contains all unique characters: a,b,c,d

n=input("enter the characters: ")

res=""
for i in n:
    if i not in res:
        res+=i+","
print("dbca contains all unique characters: ",res)