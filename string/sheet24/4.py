# 4.
# Consonant Counter in Student Name Record

# A school management system wants to count how many consonants are present in student names.

# Input: Enter student name: Ajay Singh Thakur

# Output: Total consonants: 11       // space= 12 and without space = 10

# NOTE:

# Ignore case sensitivity (treat A and a same)
# Consider only English alphabets for vowel/consonant counting
# Vowels: A, E, I, O, U

n=input("Enter student name: ").lower()

const=0
for i in n:
    # if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":     # count space also
    if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!=" ":
        const+=1
print("Total consonants: ",const)