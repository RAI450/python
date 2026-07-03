
# Question 3: Online Shopping System
# Scenario

# An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

# Requirements

# Create a class named Product with:

# product_id
# product_name
# quantity
# price_per_item

# Initialize the values using a constructor.

# Calculations
# Total Amount = Quantity × Price Per Item
# If Total Amount > ₹5000, Discount = 10%
# Otherwise, Discount = 5%
# Final Amount = Total Amount − Discount
# Sample Input
# Enter Product ID : P101
# Enter Product Name : Laptop
# Enter Quantity : 2
# Enter Price Per Item : 35000
# Sample Output
# ------ Shopping Bill ------
# Product ID        : P101
# Product Name      : Laptop
# Quantity          : 2
# Price Per Item    : 35000.0
# Total Amount      : ₹70000.0
# Discount          : ₹7000.0
# Final Amount      : ₹63000.0

class product:
    def __init__(self,id,name,qun,pri):
        self.product_id=id
        self.product_name=name
        self.quantity=qun
        self.price_per_item=pri

    def amt(self):
        return self.quantity * self.price_per_item
    def disc(self):
        if self.amt()>5000:
            return 0.1*self.amt()
        else:
            return 0.05*self.amt()
    def famt(self):
        return self.amt()-self.disc()
    def display(self):
        print("------ Shopping Bill ------")
        print("Product ID   : ",self.product_id)
        print("product Name   : ",self.product_name)
        print("quantity   : ",self.quantity)
        print("Price Per Item    : ",self.price_per_item)
        print("total amount   : ",self.amt())
        print("discount   : ",self.disc())
        print("final amount   : ",self.famt())


pid=int(input("enter the id: "))
name=input("enter the name: ")
qun=int(input("enter the quantity: "))
pri=int(input("enter the price: "))
s=product(pid,name,qun,pri)
s.display()
