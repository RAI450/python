# 6. Banking Fraud Detection System

# A bank checks fraud risk based on transaction amount, location, device, and transaction count.

# If amount is greater than or equal to 50000, then check location. If location is international, then check device.
# If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. 
# If device is not new, mark Medium Risk.

# If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

# If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk.
# If no unusual activity, mark Safe.

# Input:
# Amount = 70000
# Location = international
# Device = new
# Transactions = 4

# Output:
# Risk Level = High Risk (Blocked)

amt=int(input("enter amout "))
lcn=input("enter location ")
dvc=input("enter device ")
trns=int(input("enter transaction count "))

if amt>=50000:
    if lcn=="international":
        if dvc=="new":
            if trns>3:
                print("High Risk (Block)")
            else:
                print("medium risk")
        else:
            print("medium risk")
    if lcn=="domestic":
        if trns>5:
            print("medium risk")
        else:
            print("low risk")
else:
    if lcn=="unusual":            #---------------???????????????????????????
        if dvc=="new":
            print("medium risk")
        else:
            print("low risk")
    else:
        print("safe")

            