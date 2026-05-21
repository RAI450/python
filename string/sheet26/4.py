# 4.  Instant Messaging Word Encryption System

# A messaging application wants to temporarily encrypt messages during
# transmission. The encryption rule is to reverse every word individually
# while keeping the word positions unchanged.

# Input: Enter message: java is powerful

# Output: Encrypted Message: avaj si lufrewop

n=input("Enter message: ")

s=n.split()
t=""
for i in s:
    rev=""
    for j in i:
        rev=j+rev
    t=t+rev+" "

print("Encrypted Message: ",t)