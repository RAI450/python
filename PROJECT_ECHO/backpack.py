

class Backpack:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to backpack.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from backpack.")
        else:
            print("Item not found.")

    def has_item(self, item):
        return item in self.items

    def show_items(self):
        if self.items:
            print("""
================ BACKPACK ================
""")
            for item in self.items:
                print(f"- {item}")

            print("""
==========================================
""")
        else:
            print("""
================ BACKPACK ================

Backpack is empty.

==========================================
""")