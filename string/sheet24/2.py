# 2.
# Space Counter in Chat Messages

# A chat application wants to calculate how many spaces are used in a message.

# Input: Enter chat message: Good morning everyone how are you

# Output: Total spaces: 5

n=input("Enter feedback message: ").lower()

spc=0
for i in n:
    if i==" ":
        spc+=1
print("Total spaces: ",spc)