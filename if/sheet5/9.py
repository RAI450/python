# 9. Library Access System
#    A library checks:

# * If membership is active → Entry allowed
# * If books issued < 3 → Can issue more books

# Input:
# Membership active (yes/no): yes
# Books issued: 2

# Output:
# Entry allowed
# Can issue more books


mem=input("Membership active (yes/no):")
book=int(input("Books issued:"))

if mem=="yes":
    print("entry allowed")
    if book<3:
        print("can issue more books")