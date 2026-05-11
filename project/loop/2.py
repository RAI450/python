#GYM PLANNER

# --------------------------welcome screen----------------------------------
a="="*30
print(a,end="")
print()
print(" WELCOME T0 RAI'S GYM ")
print(a,end="")
print()

# ----------------------------main menu--------------------------------------------
print('''MENU OPTIONS:
        1 → Sign up
        2 → Login
        3 → Exit''')
z=False
while True:
    ch=int(input("enter your choice: "))                       #ch-choice 
    if ch==2 and z==False:
        print("Sign Up First Please")
    else:
        match ch:
            case 1:
                #-----------------------------SIGN UP----------------------------------------
                print(a,end="")
                print()
                print(" SIGNUP PAGE ")
                print(a,end="")
                print()
                name=input("Enter Name: ").upper()
                age=int(input("Enter Age: "))
                gender=input("enter your gender- ")
                un=input("Create Username: ").lower()                #un-username
                pswd=input("Create Password: ")                      #pswd-password
                cpswd=input("confirm Password: ")                    #cpswd-confirm password
                while True:
                    if len(str(pswd))>=6 and (pswd==cpswd):
                        print("\npassword created successfully")
                        break
                    elif len(str(pswd))<6:                  
                        print("password length should be greater then six ")
                    else:
                        print("password and confirm password not match")
                    pswd=input("Create Password: ")
                    cpswd=input("confirm Password: ")
                print()
                z=True
            
            case 2:
                # ---------------------------Login Page-------------------------------------------
                print(a,end="")
                print()
                print("   LOGIN PAGE ")
                print(a,end="")
                print()
                
                while True:
                    s_un=input("Enter Username: ").lower()
                    s_pswd=input("Enter Password: ")
                    if (s_un==un) and (s_pswd==pswd):
                        print("Login Sucessful.")
                        print("welcome ",name," to RAI's GYM\n")
                        break
                    else:
                        print("Invalid Credentials")
                
                while True:
                    w=float(input("enter your weight(in kg): "))
                    h=float(input("enter your height(in m): "))
                    if h<=0 or w<=0:
                        print("INVALID DATA!!!")
                        print("ENTER AGAIN")
                        break
                    else:

                        bmi=w/h**2
                        if bmi < 18.5:
                            print("Underweight")
                            print("RECOMMENDATION- BUILD MUSCLE")

                        elif bmi >= 18.5 and bmi < 25:
                            print("Normal")
                            print("RECOMMENDATION- MAINTAIN FITNESS")

                        elif bmi >= 25 and bmi < 30:
                            print("Overweight")
                            print("RECOMMENDATION- FAT LOSS")

                        else:
                            print("Obese")
                            print("RECOMMENDATION- SAFE WEIGHT REDUCTION")

                
                print('''MENU OPTIONS FOR GOAL:
        1 → Weight Loss
        2 → Muscle Gain
        3 → Maintain Fitness
        4 → Increase Stamina
        5 → Exit''')
                while True:
                    goal=int(input("enter your goal: "))
                    match goal:
                        case 1:
                            print("you choosed weight loss")
                            print("Generating Your Workout Plan.....")
                            print('''
    MONDAY~
        -push-ups
        -squats
        -dumbell curls
        -light jogging\n
    TUESDAY~
        -chest exercises
        -shoulder exercises
        -stretching\n
    WEDNESDAY~
        -rest or light walking\n
    THURSDAY~
        -leg workout
        -lunges
        -step-ups\n
    FRIDAY~
        -full body workout
        -pull exercises
        -core exercises\n
    SATURDAY~
        -light cardio
        -cycling
        -yoga\n
    SUNDAY~
        -rest day\n
                                  ''')
                            break
                        case 2:
                            print("you choosed Muscle Gain")
                            print("Generating Your Workout Plan.....")
                            print('''
    MONDAY~
        -running
        -push-ups
        -squats\n
    TUESDAY~
        -yoga
        -stretching
        -yoga\n
    WEDNESDAY~
        -cardio exercises
        -cycling\n
    THURSDAY~
        -upper body workout\n
    FRIDAY~
        -lower body workout\n\n
    SATURDAY~
        -sports activity
        -jump rope\n
    SUNDAY~
        -rest day\n
                                  ''')
                            break
                        case 3:
                            print("you choosed weight loss")
                            print("Generating Your Workout Plan.....")
                            print('''
    MONDAY~
        -fast working
        -jump rope
        -cardio\n
    TUESDAY~
        -full body workout
        -light weights\n
    WEDNESDAY~
        -cycling
        -jogging\n
    THURSDAY~
        -HIIT beginner workout\n
    FRIDAY~
        -core workout
        -plank
        -mountain climbers\n
    SATURDAY~
        -stretching
        -yoga\n
    SUNDAY~
        -walking\n
                                  ''')
                            break
                        case 4:
                            print("you choosed weight loss")
                            print("Generating Your Workout Plan.....")
                            print('''
    MONDAY~
        -slow walking
        -stretching\n
    TUESDAY~
        -beginner yoga
        -breathing exercises\n
    WEDNESDAY~
        -light cycling\n
    THURSDAY~
        -walking
        -mobility exercises\n
    FRIDAY~
        -chair exercises
        -low impact cardio\n
    SATURDAY~
        -meditation
        -yoga\n
    SUNDAY~
        -rest\n
                                  ''')
                            break
                        case 5:
                            print("Redirecting back...")
                            break
                        case _:
                            break

            case 3:
                ext=input("Are You Sure Want To Exit?(yes/no)").lower()
                if ext=="yes":
                    print("THANK YOU FOR COMING !!!!")
                    print("PLEASE, COME AGAIN SOONER")
                    break
                else:
                    print("redirecting to main menu....")
            case _:
                print("INVALID CHOICE. CHOOSE AGAIN")
