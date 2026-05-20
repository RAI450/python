# Mobile Number Digit Counter

# A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

# Input:
# Enter contact number: +91 98765-43210

# Output:
# Total digits: 12


n=input("enter contacts number: ")

count=0
for i in n:
    a=ord(i)
    if a>=48 and a<=57:
        count+=1
    
print("total digits= ",count)