# 2. Student Performance Analyzer
#    A school wants to evaluate students based on marks.

# * If marks ≥ 40 → Pass
# * If marks ≥ 75 → Distinction

# Input:
# Enter marks: 80

# Output:
# Pass
# Distinction

m=int(input("enter your marks"))

if m>=40:
    print("pass")

if m>=75:
    print("distinction")

if m<40:
    print("fail")