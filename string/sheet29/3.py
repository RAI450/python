# # 3. Secure Banking Transaction Analyzer

# A banking server generates encrypted transaction IDs using letters and digits.

# The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

# If no unique digit exists, print:
# text
# No unique digit found

# ### Input:
# text
# A122334455667789

# ### Output:
# text
# 8

n=input("enter the string: ")

l=len(n)
res=""
for i in n:
    count=0
    if ord(i)>=48 and ord(i)<=57:
        for j in n:
            if i==j:
                count+=1
        if count==1:
            res+=i
print(res[0])
            
