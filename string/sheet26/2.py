# 2.  Corporate Employee Short ID Generator

# A multinational company wants to automatically generate short IDs for
# employees while creating official email accounts. The system should take
# the employee’s full name and create an ID using the first character of
# each word.

# Conditions: - Take first character of every word - Convert all
# characters to uppercase

# Input: Enter employee name: ajay singh thakur

# Output: Employee Short ID: AST

n=input("Enter employee name: ")

s=n.split()
print(s)
srt=""
for i in s:
    for j in range(1):
        srt=srt+i[0]
print("employee short id: ",srt.upper())