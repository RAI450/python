

bil=[]
def total_amount(a,b,c):
    tbil=a+b+c
    return tbil
def dis_bill():
    for i in bil:
        for k,v in i.items():
            print(k," : ",v)
        print()
        

def generate_bill():
    bdic={}
    bdic["pid"]=int(input("enter the patient id: "))
    bdic["cc_rg"]=int(input("enter the consultant charges: "))
    bdic["md_cst"]=int(input("enter the medicine cost: "))
    bdic["tst_chrg"]=int(input("enter the test charges: "))
    bdic["tbil"]=total_amount(bdic["cc_rg"],bdic["md_cst"],bdic["tst_chrg"])
    bil.append(bdic)
    dis_bill()


# #----------------------chatgpt version-------------------

# bil = []

# def total_amount(a, b, c):
#     return a + b + c


# def generate_bill():

#     dic = {}

#     dic["pid"] = int(input("Enter Patient ID: "))
#     dic["consultation"] = int(input("Enter Consultation Charges: "))
#     dic["medicine"] = int(input("Enter Medicine Cost: "))
#     dic["test"] = int(input("Enter Test Charges: "))

#     dic["total_bill"] = total_amount(
#         dic["consultation"],
#         dic["medicine"],
#         dic["test"]
#     )

#     bil.append(dic)

#     print("\nGenerated Bill\n")

#     for k, v in dic.items():
#         print(f"{k} : {v}")

#     print()