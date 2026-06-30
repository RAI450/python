# Assignment: Hospital Management System Using Python Packages and Modules

# Problem Statement:

# Develop a menu-driven Hospital Management System application in Python.

# The application should be developed using proper packages and modules. 
# Do not write the complete program in a single file. Divide the application
# into different packages based on functionality.

# Project Structure:

# HospitalManagement/

#     main.py

#     patient/
#         __init__.py
#         patient_module.py

#     doctor/
#         __init__.py
#         doctor_module.py

#     appointment/
#         __init__.py
#         appointment_module.py

#     billing/
#         __init__.py
#         billing_module.py


# Requirements:

# 1. Patient Management Package

# Create a package named "patient".

# Create module:
# patient_module.py


# Implement the following functions:

# a) add_patient()

# Take patient details from user:

# - Patient ID
# - Patient Name
# - Age
# - Gender
# - Disease
# - Mobile Number


# Store patient information using list and dictionary.


# b) display_patients()

# Display all registered patients.


# c) search_patient()

# Search patient details using Patient ID.


# --------------------------------------------------


# 2. Doctor Management Package

# Create a package named "doctor".

# Create module:
# doctor_module.py


# Implement the following functions:


# a) add_doctor()

# Take doctor details:

# - Doctor ID
# - Doctor Name
# - Specialization
# - Experience
# - Consultation Fees


# Store doctor information using list and dictionary.


# b) display_doctors()

# Display all doctor details.


# --------------------------------------------------


# 3. Appointment Management Package

# Create a package named "appointment".

# Create module:
# appointment_module.py


# Implement:


# a) book_appointment()

# Take appointment details:

# - Appointment ID
# - Patient ID
# - Doctor ID
# - Appointment Date
# - Appointment Time


# Store appointment information.


# b) show_appointments()

# Display all booked appointments.


# --------------------------------------------------


# 4. Billing Package

# Create a package named "billing".

# Create module:
# billing_module.py


# Implement:


# generate_bill()


# Take:

# - Patient ID
# - Consultation Charges
# - Medicine Cost
# - Test Charges


# Calculate total amount:

# Total Bill = Consultation Charges + Medicine Cost + Test Charges

# Display complete bill.


# --------------------------------------------------


# 5. Main Application

# Create main.py file.

# Create a menu-driven program.


# Menu:

# ========== Hospital Management System ==========

# 1. Add Patient
# 2. Display Patients
# 3. Search Patient
# 4. Add Doctor
# 5. Display Doctors
# 6. Book Appointment
# 7. Show Appointments
# 8. Generate Bill
# 9. Exit
# According to user choice call the required functions from packages.
# -------------------------------------------------------------------------------------------------


from patient.patient_module import add_patient, display_patients, search_patient
from doctor.doctor_module import add_doctor, display_doctors
from appointment.appointment_module import book_appointment, show_appointments
from billing.billing_module import generate_bill

while True:
    print("""
========== Hospital Management System ==========

1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit
--------------------------------------------------
        """)
    n=int(input("enter the choice: "))
    match n:
        case 1:
            add_patient()
        case 2:
            display_patients()
        case 3:
            pid=int(input("enter the patient id: "))
            search_patient(pid)
        case 4:
            add_doctor()
        case 5:
            display_doctors()
        case 6:
            book_appointment()
        case 7:
            show_appointments()
        case 8:
            generate_bill()
        case 9:
            print("thank you...")
            break
        case _:
            print("enter the valid choice")


# # 2nd way--------------------------------------------------------------

# from patient import patient_module
# from doctor import doctor_module
# from appointment import appointment_module
# from billing import billing_module

# while True:
#     print("""
# ========== Hospital Management System ==========

# 1. Add Patient
# 2. Display Patients
# 3. Search Patient
# 4. Add Doctor
# 5. Display Doctors
# 6. Book Appointment
# 7. Show Appointments
# 8. Generate Bill
# 9. Exit
# --------------------------------------------------
#         """)
#     n=int(input("enter the choice: "))
#     match n:
#         case 1:
#             patient_module.add_patient()                         #CALLING
#         case 2:
#             patient_module.display_patients()
#         case 3:
#             pid=int(input("enter the patient id: "))
#             patient_module.search_patient(pid)
#         case 4:
#             doctor_module.add_doctor()
#         case 5:
#             doctor_module.display_doctors()
#         case 6:
#             appointment_module.book_appointment()
#         case 7:
#             appointment_module.show_appointments()
#         case 8:
#             billing_module.generate_bill()
#         case 9:
#             print("thank you...")
#             break
#         case _:
#             print("enter the valid choice")