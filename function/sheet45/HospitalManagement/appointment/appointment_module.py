
a_dtl=[]
def book_appointment():
    adic={}
    adic["aid"]=int(input("enter the appointment id: "))
    adic["pid"]=int(input("enter the patient id: "))
    adic["did"]=int(input("enter the doctor id: "))
    adic["date"]=input("enter the appointment date(DD/MM/YYYY): ")
    adic["time"]=input("enter the appointment time: ")
    a_dtl.append(adic)
    print("Appointment booked successfully.")

def show_appointments():
    for i in a_dtl:
        for k,v in i.items():
            print(k," : ",v)
        print()

# #----------------------chatgpt version-------------------

# a_dtl = []

# def book_appointment():

#     dic = {}

#     dic["aid"] = int(input("Enter Appointment ID: "))
#     dic["pid"] = int(input("Enter Patient ID: "))
#     dic["did"] = int(input("Enter Doctor ID: "))
#     dic["date"] = input("Enter Appointment Date (DD/MM/YYYY): ")
#     dic["time"] = input("Enter Appointment Time: ")

#     a_dtl.append(dic)

#     print("Appointment booked successfully.\n")


# def show_appointments():

#     if not a_dtl:
#         print("No appointments found.\n")
#         return

#     for i in a_dtl:
#         for k, v in i.items():
#             print(f"{k} : {v}")
#         print()