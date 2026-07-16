class Item:
    """Represents one collectible item (mainly the key cards / rewards
    the player picks up after solving a room's puzzle)."""

    def __init__(self, name, description, usable=True):
        self.name = name
        self.description = description
        self.usable = usable

    def show_item(self):
        print(f"""
================ ITEM =================

Name        : {self.name}
Description : {self.description}
Usable      : {"Yes" if self.usable else "No"}

=======================================
""")

    def use(self):
        """Simulate using the item. Kept simple since the game does not
        need item combining or crafting -- just a flavor action."""
        if self.usable:
            print(f"\nYou use the {self.name}.\n{self.description}\n")
        else:
            print(f"\nThe {self.name} cannot be used right now.\n")
