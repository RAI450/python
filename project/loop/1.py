# smart routine planner

# --------------------------welcome screen----------------------------------
a="="*30
print(a,end="")
print()
print(" SMART ROUTINE PLANNER SYSTEM ")
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
                un=input("Create Username: ").lower()                #un-username
                pswd=input("Create Password: ")                      #pswd-password
                cpswd=input("confirm Password: ")                    #cpswd-confirm password
                while True:
                    if len(str(pswd))>=6 and (pswd==cpswd):
                        print("\npassword created successfully")
                        break
                    elif len(str(pswd))<6:                  
                        print("password length should be greater than six ")
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
                        print("welcome ",name,"\n")
                        break
                    else:
                        print("Invalid Credentials")

                #-----------------------------FITNESS PLAN------------------------------------------

                while True:                                               # user-premium or general
                    usr=input("Enter Premium or General- ").lower()
                    if usr=="premium":
                        print("you are a premium user and customization plans unlocked")
                        break
                    elif usr=="general":
                        print("you are a general user for customization plans upgrade to premium \n")
                        break
                    else:
                        print("please enter option correctly ")


                print('''MENU OPTIONS FOR PLAN:
1 → IDEALLY PRE-DEFINED PLANS
2 → CUSTOMIZE PLANS
3 → BACK''')
                
                plns=int(input("Choose Your Plans: "))

                match plns:
                    case 1:
                        print('''MENU OPTIONS FOR FITNESS PLAN(GENERAL):
1 → SCHOOL STUDENT
2 → COLLEGE STUDENT
3 → WORKING PROFESSIONAL
4 → FITNESS ENTHUSIAST
5 → SENIOR CITIZEN''')
                
                        ctgry=int(input("CHOOSE YOUR CATEGORY: "))
                        match ctgry:
                            case 1:
                                print("""===== IDEAL ROUTINE FOR SCHOOL STUDENT  =====

    6:00 AM  - Wake Up
    6:30 AM  - Exercise / Freshen Up
    7:00 AM  - Breakfast
    8:00 AM  - School Time
    2:30 PM  - Lunch & Rest
    4:00 PM  - Homework
    6:00 PM  - Play Time
    7:00 PM  - Revision
    9:00 PM  - Dinner
    10:00 PM - Sleep
                                      
        Focus: Discipline + Study + Physical Activity
                                      
        Health Tip: Drink at least 3 liters of water daily.
        Small daily improvements lead to big success.""")
                                
                            case 2:
                                print("""===== IDEAL COLLEGE STUDENT ROUTINE =====

    6:30 AM  - Wake Up
    7:00 AM  - Workout / Walk
    8:00 AM  - Breakfast
    9:00 AM  - College / Classes
    3:00 PM  - Skill Development
    5:00 PM  - Free Time
    6:00 PM  - Study / Assignments
    8:00 PM  - Dinner
    9:00 PM  - Project / Coding Practice
    11:00 PM - Sleep

        Focus: Career Growth + Skills + Productivity
                                      
        Health Tip: Drink at least 3 liters of water daily.
        Small daily improvements lead to big success.""")
                                
                            case 3:
                                print("""===== IDEAL WORKING PROFESSIONAL ROUTINE =====

    5:30 AM  - Wake Up
    6:00 AM  - Exercise
    7:00 AM  - Breakfast
    9:00 AM  - Office Work
    1:00 PM  - Lunch Break
    6:00 PM  - Relaxation Time
    7:00 PM  - Family Time
    8:00 PM  - Dinner
    9:00 PM  - Planning for Tomorrow
    10:30 PM - Sleep

        Focus: Work-Life Balance + Health
                                      
        Health Tip: Drink at least 3 liters of water daily.
        Small daily improvements lead to big success.""")
                                
                            case 4:
                                print("""===== IDEAL FITNESS ROUTINE =====

    5:00 AM  - Wake Up
    5:30 AM  - Cardio Workout
    7:00 AM  - Healthy Breakfast
    9:00 AM  - Work / Study
    1:00 PM  - Protein Rich Lunch
    5:00 PM  - Strength Training
    7:00 PM  - Meditation
    8:00 PM  - Healthy Dinner
    9:30 PM  - Sleep                                    

        Focus: Strength + Recovery + Nutrition
                                        
        Health Tip: Drink at least 3 liters of water daily.
        Small daily improvements lead to big success.""")
                                
                            case 5:
                                print("""===== IDEAL SENIOR CITIZEN ROUTINE =====

    6:00 AM  - Wake Up
    6:30 AM  - Morning Walk
    7:30 AM  - Healthy Breakfast
    9:00 AM  - Reading / Prayer
    12:30 PM - Lunch
    2:00 PM  - Rest
    5:00 PM  - Light Exercise / Social Time
    7:00 PM  - Dinner
    8:00 PM  - Relaxation
    9:00 PM  - Sleep

        Focus: Peaceful Lifestyle + Good Health""")
                                
                            case _:
                                print("INVALID CHOICE. CHOOSE AGAIN")  
                # ------------------------------------------------------------for customization-----------------------------
                    case 2:
                        if usr=="general":
                            print("UPGRADE TO PREMIUM TO USE THIS FEATURES ")
                        else:
                            print('''MENU OPTIONS FOR FITNESS PLAN(premium):
1 → SCHOOL STUDENT
2 → COLLEGE STUDENT
3 → WORKING PROFESSIONAL
4 → FITNESS ENTHUSIAST
5 → SENIOR CITIZEN''')
                                                                        
                            while True:
                                prfsn=int(input("Choose Your Profession: "))                #----profession
                                match prfsn:
                                    case 1:
                                        print("you are a school student")
                                        break
                                    case 2:
                                        print("you are a college student")
                                        break
                                    case 3:
                                        print("you are a working professional")
                                        break
                                    case 4:
                                        print("you are a fitness enthusiast")
                                        break
                                    case 5:
                                        print("you are a senior citizen")
                                        break
                                    case _:
                                        print("INVALID CHOICE. CHOOSE AGAIN")
                            
                            if prfsn==1 or prfsn==2:
                                stdy=float(input("How many hours do you want to study daily? "))
                            if prfsn==3:
                                wrk=float(input("Working Hours Per Day: "))
                                
                            st=float(input("Enter Your Sleep Time: "))         # sleep schedule           
                            wt=float(input("Enter Your Wakeup Time: "))
                            if wt>6.0:
                                print("Early wake-up improves productivity")
                            ts=float(input("Total Time For Sleeping- "))
                            if ts<6.0:
                                print("Sleep Alert: Less than 6 hours sleep is unhealthy")
                                print("Recommended sleep duration: 7-8 hours")
                            elif ts>9.0:
                                print("Warning: Oversleep Warning")
                                print("Recommended sleep duration: 7-8 hours") 

                            ex=input("Do You Exercise Daily?(yes/no): ").lower()   # Exercise

                            mls=int(input("Enter Meals Per Day: "))
                            wtr=int(input("Daily Water Intake(in Litres)"))
                            if wtr<3:
                                print("your water intake is low.\nDrink at least 3 liters of water daily")
                            
                            print("""
==================================
 PERSONALIZED ROUTINE GENERATING...
==================================""")
                            print('''
6:00 AM  - Wake Up
6:30 AM  - Yoga Session
7:00 AM  - Healthy Breakfast
8:00 AM  - Study Session
11:00 AM - Short Break
1:00 PM  - Lunch
2:00 PM  - Productivity Work
5:00 PM  - Exercise
7:00 PM  - Family / Relaxation Time
9:30 PM  - Sleep Preparation
                                  ''')
                            break
                        
                    case 3:
                        break   # go to 
                    case _:
                        print("INVALID CHOICE. CHOOSE AGAIN")

            case 3:
                ext=input("Are You Sure Want To Exit?(yes/no)").lower()
                if ext=="yes":
                    print("THANK YOU FOR COMING !!!!")
                    print("PLEASE, COME AGAIN SOON")
                    break
                else:
                    print("redirecting to main menu....")
            case _:
                print("INVALID CHOICE. CHOOSE AGAIN")







                
                


                
                
                



                

            
        
                    


                







