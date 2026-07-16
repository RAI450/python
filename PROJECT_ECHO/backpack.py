from utils import press_enter, print_header


class Backpack:
    """Stores the Item objects the player collects during the game."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"\n'{item.name}' has been removed from your backpack.")
        else:
            print("Item not found.")

    def has_item(self, item):
        return item in self.items

    def show_items(self):
        """Simple listing, e.g. for quick reference in the HUD."""
        print_header("Backpack")

        if self.items:
            for item in self.items:
                print(f"- {item.name}")
        else:
            print("Backpack is empty.")

        print()

    def inspect_items(self):
        """Interactive menu that lets the player pick one item and
        view its full description -- makes the backpack feel like a
        real inventory instead of a static list."""

        if not self.items:
            print_header("Backpack")
            print("Backpack is empty.\n")
            press_enter()
            return

        while True:
            print_header("Backpack")

            for index, item in enumerate(self.items, 1):
                print(f"{index}. {item.name}")

            print(f"{len(self.items) + 1}. Go Back")

            choice = input("\nEnter choice : ").strip()

            if not choice.isdigit():
                print("Invalid Choice.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(self.items):
                self.items[choice - 1].show_item()
                press_enter()

            elif choice == len(self.items) + 1:
                break

            else:
                print("Invalid Choice.")
