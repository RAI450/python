

p_dtl=[]
def add_patient():
    dic={}
    dic["pid"]=int(input("enter the patient id: "))
    dic["name"]=input("enter the patient name: ")
    dic["age"]=int(input("enter the age: "))
    dic["gender"]=input("enter the gender: ")
    dic["disease"]=input("enter the disease: ")
    dic["mobile_number"]=int(input("enter the patient mobile number: "))
    p_dtl.append(dic)
    print("Patient added successfully.")


def display_patients():
    for i in p_dtl:
        for k,v in i.items():
            print(k," : ",v)
        print()

def search_patient(pid):
    for i in p_dtl:
        if i["pid"]==pid:
            print(i)
            return
    print("patient does not exist")


# #----------------------chatgpt version-------------------

# p_dtl = []

# def add_patient():
#     dic = {}
#     dic["pid"] = int(input("Enter Patient ID: "))
#     dic["name"] = input("Enter Patient Name: ")
#     dic["age"] = int(input("Enter Age: "))
#     dic["gender"] = input("Enter Gender: ")
#     dic["disease"] = input("Enter Disease: ")
#     dic["mobile"] = input("Enter Mobile Number: ")

#     p_dtl.append(dic)
#     print("Patient added successfully.\n")


# def display_patients():
#     if not p_dtl:
#         print("No patients found.\n")
#         return

#     for i in p_dtl:
#         for k, v in i.items():
#             print(f"{k} : {v}")
#         print()


# def search_patient(pid):
#     for i in p_dtl:
#         if i["pid"] == pid:
#             print("\nPatient Found\n")
#             for k, v in i.items():
#                 print(f"{k} : {v}")
#             print()
#             return

#     print("Patient not found.\n")
