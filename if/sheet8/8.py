# 8. Smart Farming Irrigation System

# A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

# If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type.
#  If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply.
#  If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. 
# If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

# Input:
# Soil Moisture = 25
# Temperature = 36
# Crop = wheat

# Output:
# Irrigation = High Water Supply

sm=int(input("enter soil moisture "))
temp=int(input("enter temperature "))
crp=input("enter crop type ")
pre=input("rainfall prediction (expected/not)")

if sm<=30:
    if temp>=35:
        if crp=="wheat":
            print("Irrigation = High Water Supply")
        else:
            print("Irrigation = moderate Water Supply")
    else:
        print("Irrigation = moderate Water Supply")
else:
    if sm<=60:
        if pre=="expected":
            print("Irrigation = delay irrigation ")
        else:
            print("Irrigation = light irrigation ")
    else:
        print("Irrigation = no irrigation ")