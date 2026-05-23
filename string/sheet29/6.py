# # 6. AI Chat Toxic Pattern Detector

# An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

# If found:
# text
# Spam Pattern Found

# Else:
# text
# Clean Message

# ### Input:
# text
# heyyy broooo welcome

# ### Output:
# text
# Spam Pattern Found

n=input("enter the sentence: ")

l=len(n)
for i in range(1,l-1):
    a=n[i-1]
    b=n[i]
    c=n[i+1]
    if a==b==c:
        print("spam pattern detected")
        break
else:
    print("clean message")





