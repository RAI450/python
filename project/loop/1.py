# smart routine planner

# welcome screen----------------------------------------
a="="*30
print(a,end="")
print()
print(" SMART ROUTINE PLANNER SYSTEM ")
print(a,end="")
print()

# main menu--------------------------------------------
print('''menu options:
        1 → Sign up
        2 → Login
        3 → Exit''')
while True:
    ch=int(input("enter your choice: "))                       #ch-choice
    match ch:
        case 1:
            name=input("Enter Name: ").upper
            age=int(input("Enter Age: "))
            un=input("Create Username: ").lower                #un-username
            pswd=input("Create Password: ")                    #pswd-password
            cpswd=input("confirm Password: ")                  #cpswd-confirm password
            if pwsd>=6:







