# 3. E-Commerce Offer Engine
#    An online store provides multiple offers independently:

# * If cart value ≥ 500 → Free delivery
# * If cart value ≥ 1000 → 10% discount coupon

# Input:
# Enter cart value: 1200

# Output:
# Free delivery applied
# Discount coupon unlocked

val=int(input("enter cart value"))
if val>=500:
    print("free delivery applied")

if val>=1000:
    print("10% discount coupon unlocked")

if val<500:
    print("not eligible for discount or free delivery")