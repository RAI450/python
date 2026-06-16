# 1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

# A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

# The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

# Key → Patient ID
# Value → Dictionary containing patient details

# Each patient record should contain:

# Patient Name
# Age
# Gender
# Disease
# Doctor Name
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "age":35,
#     "gender":"Male",
#     "disease":"Fever",
#     "doctor":"Dr. Sharma"
# },
# 102:{
#     "name":"Ravi",
#     "age":42,
#     "gender":"Male",
#     "disease":"Diabetes",
#     "doctor":"Dr. Gupta"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =====================================
#  HOSPITAL PATIENT MANAGEMENT SYSTEM
# =====================================

# 1. Add New Patient
# 2. Search Patient
# 3. Update Patient Disease
# 4. Delete Patient Record
# 5. Display All Patients
# 6. Count Total Patients
# 7. Display Patients By Disease
# 8. Display Oldest Patient
# 9. Display Youngest Patient
# 10. Exit

# Functional Requirements
# 1. Add New Patient

# Accept the following information from the user:

# Patient ID
# Patient Name
# Age
# Gender
# Disease
# Doctor Name

# Store the record in the nested dictionary.

# Validation:
# If the Patient ID already exists, display:

# Patient ID already exists.

# 2. Search Patient

# Accept Patient ID from the user.

# If the patient exists, display complete information.

# Sample Output

# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Gender     : Male
# Disease    : Fever
# Doctor     : Dr. Sharma

# If Patient ID is not found:

# Patient Record Not Found

# 3. Update Patient Disease

# Accept Patient ID.

# If found:

# Ask for new disease.
# Update the disease information.

# Sample Output

# Disease Updated Successfully
# 4. Delete Patient Record

# Accept Patient ID.

# If found:

# Remove the patient record.

# Sample Output

# Patient Record Deleted Successfully

# Otherwise:

# Patient Not Found
# 5. Display All Patients

# Display all patient records in a formatted manner.

# Sample Output

# --------------------------------
# Patient ID : 101
# Name       : Ajay
# Age        : 35
# Disease    : Fever
# Doctor     : Dr. Sharma
# --------------------------------

# Patient ID : 102
# Name       : Ravi
# Age        : 42
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 6. Count Total Patients

# Display the total number of patients currently stored.

# Sample Output

# Total Patients : 25
# 7. Display Patients By Disease

# Accept a disease name from the user.

# Display all patients suffering from that disease.

# Sample Output

# Enter Disease : Fever

# 101  Ajay
# 108  Aman
# 115  Neha

# If no patient is found:

# No Patient Found
# 8. Display Oldest Patient

# Find and display the patient having the highest age.

# Sample Output

# Oldest Patient Details

# Patient ID : 110
# Name       : Ravi
# Age        : 68
# Disease    : Diabetes
# Doctor     : Dr. Gupta
# 9. Display Youngest Patient

# Find and display the patient having the minimum age.

# Sample Output

# Youngest Patient Details

# Patient ID : 121
# Name       : Riya
# Age        : 4
# Disease    : Viral Fever
# Doctor     : Dr. Mehta
# 10. Exit

# Terminate the application.

# Sample Output

# Thank You For Using Hospital Patient Management System


dt={}

while True:
    print("""
    =====================================
    HOSPITAL PATIENT MANAGEMENT SYSTEM
    =====================================

    1. Add New Patient
    2. Search Patient
    3. Update Patient Disease
    4. Delete Patient Record
    5. Display All Patients
    6. Count Total Patients
    7. Display Patients By Disease
    8. Display Oldest Patient
    9. Display Youngest Patient
    10. Exit
        """)

    n=int(input("enter the choice: "))
   
    match n:
        case 1:
            print("adding new patient---")
            
            pid=int(input("enter the patient id: "))
            if pid not in dt:
                name=input("enter the name: ")
                age=int(input("enter the age: "))
                gen=input("enter the gender: ")
                dis=input("enter the disease: ")
                dnme=input("enter the doctor name: ")

                dt[pid]={
                    "name": name,
                    "age": age,
                    "gender": gen,
                    "disease": dis,
                    "doctor_Name": dnme
                }
            else:
                print("Patient ID already exists")
        
        case 2:
            pid=int(input("enter the patient id: "))
            if pid in dt:
                print("patient id : ",pid)
                for k,v in dt[pid].items():
                    print(k,"   : ",v)
            else:
                print("patient id not found")
        case 3:
            pid=int(input("enter the patient id: "))
            if pid in dt:
                ndis=input("enter the new disease: ")
                dt[pid]["disease"]=ndis
                print("disease updated successfully")
            else:
                print("patient id not found")

        case 4:
            pid=int(input("enter the patient id: "))
            if pid in dt:
                del dt[pid]
                print("patient record deleted successfully")
            else:
                print("patient id not found")
        case 5:
            if len(dt) == 0:
                print("No patients found")
            else:
                for i in dt:
                    print("---------------------------")
                    print("patient id : ",i)
                    for k,v in dt[i].items():
                        print(k,"   : ",v)
                print("---------------------------")
        
        case 6:
            
            print("total patients :",len(dt))
        
        case 7:
            ds=input("enter the disease: ")
            flag=False
            for i in dt:
                if dt[i]["disease"]==ds:
                    flag=True
                    print(i," ",dt[i]["name"])
            if flag==False:
                print("no patient found")

        case 8:
            if len(dt) == 0:
                print("No patients found")
            else:
                p=0
                a=0
                for i in dt:
                    if dt[i]["age"]>a:
                        a=dt[i]["age"]
                        p=i
                print("oldest patients details")
                print("patient id : ",p)
                for k,v in dt[p].items():
                        print(k,"   : ",v)
        case 9:
            if len(dt) == 0:
                print("No patients found")
            else:
                p=0
                a=float('inf')
                for i in dt:
                    if dt[i]["age"]<a:
                        a=dt[i]["age"]
                        p=i
                print("youngest patients details")
                print("patient id : ",p)
                for k,v in dt[p].items():
                        print(k,"   : ",v)


        case 10:
            print("Thank you for using hospital patient management system")
            break
        case _:
            print("Invalid choice. Please enter 1 to 10.")

