# 5. Banking Security System
#    A bank validates login attempt:

# * If username is "admin" → Valid user
# * If password length ≥ 8 → Strong password

# Input:
# Enter username: admin
# Enter password: secure123

# Output:
# Valid user
# Strong password

un,pas =input("enter username and password").split()

if un=="admin":
    print("valid user")
    if len(pas)>=8:
        print("strong password")