# 5. Smart Warehouse Dispatch System

# A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

# If stock is at least 100, then check priority. If high priority, then check distance. 
# If distance is up to 200, dispatch immediately; otherwise use fast courier. 
# If priority is not high, then check if stock is at least 300. 
# If yes, bulk dispatch; otherwise normal dispatch. 
# If stock is less than 100, then check if stock is at least 50. 
# If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

# Input:
# Stock = 120
# Priority = high
# Distance = 300

# Output:
# Dispatch Status = Dispatch via Fast Courier

sto=int(input("enter stock "))
pri=input("enter priority ")
dis=int(input("enter distance"))

if sto>=100:
    if pri=="high":
        if dis<=200:
            print("dispatch status = dispatch immediately ")
        else:
            print("dispatch status = fast courier ")
    else:
        if sto>=300:
            print("dispatch status = bulk dispatch ")
        else:
            print("dispatch status = normal dispatch")
elif sto>=50:
    if pri=="high":
        print("dispatch status = partially dispatch ")
    else:
        print("dispatch status = hold ")
else:
    print(" mark out of stock ")


