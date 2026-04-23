# 2. Hospital Emergency Priority System

# A hospital assigns treatment priority based on age, severity, and insurance.

# If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

# If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

# If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

# Input:
# Age = 65
# Severity = critical
# Insurance = yes

# Output:
# Treatment = Immediate ICU

age=int(input("enter age "))
sev=input("enter severity (moderate/low/critical)")
ins=input("enter insurance (yes/no)")

if sev=="critical":
    if age>=60:
        print("treatment = Immediate ICU")
    else:
        print("treatment = emergency ward")
if sev=="moderate":
    if ins=="yes":
        print("treatment = priority treatment")
    else:
        print("treatment = general queue")
if sev=="low":
    if age<10:
        print("treatment = pediatric priority")
    else:
        print("treatment = wait")

