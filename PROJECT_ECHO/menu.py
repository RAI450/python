from utils import press_enter, print_header, get_int_choice
from data import story1, instructions, credits


class Menu:

    def show_main_menu(self):
        print_header("Main Menu")

        print("""                        1. New Game
                        2. Story
                        3. Instructions
                        4. Credits
                        5. Exit
""")

        return get_int_choice("\nPlease enter your choice : ", 1, 5)

    def show_story(self):
        story1()
        press_enter()

    def show_instructions(self):
        instructions()
        press_enter()

    def show_credits(self):
        credits()
        press_enter()

    def confirm_exit(self):
        while True:
            choice = input("Are you sure you want to exit? (y/n): ").strip().lower()

            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid Input!")
