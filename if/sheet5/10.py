# 10. Online Exam System
#     System evaluates exam conditions:

# * If marks ≥ 40 → Pass
# * If attendance ≥ 75 → Eligible for certificate

# Input:
# Enter marks: 60
# Enter attendance: 80

# Output:
# Pass
# Eligible for certificate

mark=int(input("enter your marks"))
attn=int(input("enter attendence"))

if mark>=40:
    print("pass")
    if attn>=75:
        print("eligible for certificate")