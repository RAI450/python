# 3.Smart Banking System

# Scenario:
# You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

# Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

# 👉 Important Condition:
# If no amount has been deposited yet, the system should display:
# "No balance available. Please deposit first"
# and should not allow withdrawal, balance check, or interest calculation.

# The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

# Menu Options:
# 1 → Deposit Money
# 2 → Withdraw Money
# 3 → Check Balance
# 4 → Apply Interest

# * Balance > 50000 → 5% interest
# * Otherwise → 3% interest
#   5 → Exit

# ---

# Sample Run 1:
# Input:
# Enter your choice: 2

# Output:
# No balance available. Please deposit first

# ---

# Sample Run 2:
# Input:
# Enter your choice: 1
# Enter amount to deposit: 10000

# Output:
# Amount deposited successfully

# ---

# Sample Run 3:
# Input:
# Enter your choice: 3

# Output:
# Current Balance: 10000

# ---

# Sample Run 4:
# Input:
# Enter your choice: 2
# Enter amount to withdraw: 15000

# Output:
# Insufficient balance

# ---

# Sample Run 5:
# Input:
# Enter your choice: 4

# Output:
# Interest added: 300
# Updated Balance: 10300

# ---

# Sample Run 6:
# Input:
# Enter your choice: 2
# Enter amount to withdraw: 5000

# Output:
# Withdrawal successful

# ---

# Sample Run 7 (Invalid Choice):
# Input:
# Enter your choice: 9

# Output:
# Invalid choice. Please try again.

# ---

# Sample Run 8 (Exit):
# Input:
# Enter your choice: 5

# Output:
# Exiting system... Thank you!

dpst=None
print("""menu options:
      1 → Deposit Money
      2 → Withdraw Money
      3 → Check Balance
      4 → Apply Interest
      5 → Exit """)
while True:
    
    c=int(input("enter your choice: "))
    if c>1 and dpst==None:
        print("no balance available. please deposit first")
    else:
        match c:
            case 1:
                dpst=int(input("enter amount to deposit "))
                print("amount deposited successfully")
            case 2:
                wdrw=int(input("enter amoungt to withdraw "))
                if wdrw<=dpst:
                    print("withdraw successfully")
                    dpst=dpst-wdrw
                else:
                    print("insufficient balance")
                
            case 3:
                print("current balance: ",dpst)
            case 4:
                if dpst>50000:
                    inst=int((dpst*5)/100)
                else:
                    inst=int((dpst*3)/100)
                print("intrest added: ",inst)
                print("balance updated: ",(dpst+inst))
            case 5:
                print("exiting system... Thank you!")
                break
            case _:
                print("invalid choice. please try again")
                


