# Question 2: Electricity Bill Calculator
# Scenario


# An electricity company wants to generate monthly bills for its customers.

# Requirements

# Create a class named Customer with:

# customer_id
# customer_name
# units_consumed

# Initialize the values using a constructor.

# Calculations
# Cost per Unit = ₹8
# Fixed Charge = ₹150
# Total Bill = (Units × 8) + 150
# Sample Input
# Enter Customer ID : C101
# Enter Customer Name : Amit Verma
# Enter Units Consumed : 350
# Sample Output
# ------ Electricity Bill ------
# Customer ID       : C101
# Customer Name     : Amit Verma
# Units Consumed    : 350
# Total Bill Amount : ₹2950.0

class customer:
    def __init__(self,id,name,con):
        self.customer_id=id
        self.customer_name=name
        self.customer_consumed=con
    
    def bill(self):
        return self.customer_consumed * 8 + 150
    
    def dis(self):
        print("------ Electricity Bill ------")
        print("Customer ID     : ",self.customer_id)
        print("Customer name     : ",self.customer_name)
        print("units consumed     : ",self.customer_consumed)
        print("TOTAL Bill Amount     : ",self.bill())

cid=int(input("enter the id: "))
name=input("enter the name: ")
con=int(input("enter the units consumed: "))

s1=customer(cid,name,con)
s1.dis()




