# 8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
#  The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
#  and determine which unit has the maximum stock. Display the highest stock value among all six units.

# Input:
# Unit1 = 120
# Unit2 = 450
# Unit3 = 300
# Unit4 = 275
# Unit5 = 500
# Unit6 = 390

# Output:
# Highest Stock = 500

u1,u2,u3,u4,u5,u6=map(int,input("enter quantity of items in all units").split())


# compare between half and half-------------------------------------------------

# if u1>u2:         #compare b/w 1,2 and 3
#     if u1>u3:
#         h1=u1
#     else:
#         h1=u3
# else:
#     if u2>u3:
#         h1=u2
#     else:
#         h1=u3

# if u4>u5:         #compare b/w 4,5 and 6
#     if u4>u6:
#         h2=u4
#     else:
#         h2=u6
# else:
#     if u5>u6:
#         h2=u5
#     else:
#         h2=u6

# if h1>h2:      #compare b/w h1 and h2
#     high=h1
# else:
#     high=h2

# print("highest stock = ",high)


# use of only if-------------------------------------------------------

# if u1>u2 and u1>u3 and u1>u4 and u1>u5 and u1>u6:
#     h1=u1
# if u2>u1 and u2>u3 and u2>u4 and u2>u5 and u2>u6:
#     h1=u2
# if u3>u1 and u3>u2 and u3>u4 and u3>u5 and u3>u6:
#     h1=u3
# if u4>u1 and u4>u2 and u4>u3 and u4>u5 and u4>u6:
#     h1=u4
# if u5>u1 and u5>u3 and u5>u4 and u5>u2 and u5>u6:
#     h1=u5
# if u6>u1 and u6>u3 and u6>u4 and u6>u2 and u6>u5:
#     h1=u6

# print("highest stock = ",h1)


# comparison of one by one-------------------------------------------------------

# if u1>u2:
#     if u1>u3:
#         if u1>u4:
#             if u1>u5:
#                 if u1>u6:
#                     hig=u1
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
#         else:
#             if u4>u5:
#                 if u4>u6:
#                     hig=u4
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
#     else:
#         if u3>u4:
#             if u3>u5:
#                 if u3>u6:
#                     hig=u3
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
#         else:
#             if u4>u5:
#                 if u4>u6:
#                     hig=u4
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
# else:
#     if u2>u3:
#         if u2>u4:
#             if u2>u5:
#                 if u2>u6:
#                     hig=u2
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6    
#         else:
#             if u4>u5:
#                 if u4>u6:
#                     hig=u4
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
#     else:
#         if u3>u4:
#             if u3>u5:
#                 if u3>u6:
#                     high=u3
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
#         else:
#             if u4>u5:
#                 if u4>u6:
#                     hig=u4
#                 else:
#                     hig=u6
#             else:
#                 if u5>u6:
#                     hig=u5
#                 else:
#                     hig=u6
# print("highest stock = ",hig)