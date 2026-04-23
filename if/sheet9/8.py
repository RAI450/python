# 8. E-Commerce Dynamic Pricing System

# An e-commerce system gives discount based on demand, stock, user type, and festival.

# If demand is 80 or above, then check stock. If stock is less than 50, then check user type.
# If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%.
# If user is not premium, no discount. If stock is 50 or more, give 5% discount.
# If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

# If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

# Input:
# Demand = 85
# Stock = 40
# User Type = premium
# Festival = yes

# Output:
# Discount = 20%

dmnd=int(input("enter demand "))
stk=int(input("enter stock "))
type=input("enter user type ")
fstvl=input("enter (yes/no) ")

if dmnd>=80:
    if stk<50:
        if type=="premium":
            if fstvl=="yes":
                print("discount = 20%")
            else:
                print("discount = 10%")
        else:
            print("no discount")
    else:
        print("discount = 5%")
elif dmnd>=40 and dmnd<=79:
    if fstvl=="yes":
        print("discount = 10%")
    else:
        print("no discount")
else:
    if stk>=200:
        print("discount = 15%")
    else:
        print("no discount")
