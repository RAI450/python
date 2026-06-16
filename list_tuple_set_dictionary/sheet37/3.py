# QUESTION 3: HOSPITAL PATIENT TRACKER
# ====================================

# A hospital stores patient records for daily monitoring.

# Fields:
# patient_id, patient_name, age, disease

# Requirements:

# 1. Read N patient records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all patient details.

# ---

# 3. Display patients whose age is above 60 years.

# ---

# 4. Search for a patient using Patient ID.

# ---

# 5. Count the number of patients suffering from a particular disease.

# ---

# Test Case:

# Input:
# Enter number of patients: 4

# P101 Rajesh 65 Diabetes
# P102 Suman 45 Fever
# P103 Mohan 70 Diabetes
# P104 Rita 35 Cold

# Enter Patient ID: P103
# Enter Disease: Diabetes

# Expected Output:
# Patient Found:
# P103 Mohan 70 Diabetes

# Patients Above 60:
# P101 Rajesh 65 Diabetes
# P103 Mohan 70 Diabetes

# Patients with Diabetes:
# 2


from collections import namedtuple

hos=namedtuple("hos",["patient_id", "patient_name", "age", "disease"])

n=int(input("enter the number of patients: "))

s=[]
for i in range(1,n+1):
    id=input("enter the id for patient "+str(i)+" :")
    nm=input("enter the name of patient "+str(i)+" :")
    age=int(input("enter the age of patient "+str(i)+" :"))
    dis=input("enter the disease of patient "+str(i)+" :")
    s.append(hos(id,nm,age,dis))

for i in s:
    print(i.patient_id, i.patient_name, i.age, i.disease)

pid=input("enter the patient id: ")
pd=input("enter disease: ")

for i in s:
    if i.patient_id==pid:
        print("patient found")
        print(i.patient_id, i.patient_name, i.age, i.disease)
        break
else:
    print("not found")
count=0
for i in s:
    if i.age>60:
        print("Patients Above 60: ",i.patient_id, i.patient_name, i.age, i.disease)
    if i.disease==pd:
        count+=1

print("patient with ",pd," : ",count)