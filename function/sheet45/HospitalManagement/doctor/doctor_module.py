

d_dtl=[]
def add_doctor():
    ddic={}
    ddic["did"]=int(input("enter the id of doctor: "))
    ddic["name"]=input("enter the name of doctor: ")
    ddic["spc"]=input("enter the specialization of doctor: ")
    ddic["exp"]=int(input("enter the experience of doctor: "))
    ddic["fees"]=int(input("enter the Consultation Fees of doctor: "))
    d_dtl.append(ddic)
    print("doctor added successfully")

def display_doctors():
    for i in d_dtl:
        for k,v in i.items():
            print(k," : ",v)
        print()

# #----------------------chatgpt version-------------------

# d_dtl = []

# def add_doctor():
#     dic = {}

#     dic["did"] = int(input("Enter Doctor ID: "))
#     dic["name"] = input("Enter Doctor Name: ")
#     dic["specialization"] = input("Enter Specialization: ")
#     dic["experience"] = int(input("Enter Experience (Years): "))
#     dic["fees"] = int(input("Enter Consultation Fees: "))

#     d_dtl.append(dic)

#     print("Doctor added successfully.\n")


# def display_doctors():

#     if not d_dtl:
#         print("No doctors available.\n")
#         return

#     for i in d_dtl:
#         for k, v in i.items():
#             print(f"{k} : {v}")
#         print()