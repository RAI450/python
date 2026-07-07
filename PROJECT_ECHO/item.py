class Item:

    def __init__(self, name, description, usable=True):
        self.name = name
        self.description = description
        self.usable = usable

    def show_item(self):
        print(f"""
================ ITEM =================

Name        : {self.name}      
Description : {self.description}

Usable      : {self.usable}

=======================================
""")