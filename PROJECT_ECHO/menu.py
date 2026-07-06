from utils import press_enter
from data import story1,instructions,credits

class Menu():

    def show_main_menu(self):
        while True:
            print("""
                        ===== MAIN MENU =====

                1. New Game
                2. Story
                3. Instructions
                4. Credits
                5. Exit

            --------------------------------------------------------------
            """)
            n=int(input("please enter your choice: "))

            match n:

                case 1:
                    return 1

                case 2:
                    return 2
                
                case 3:
                    return 3

                case 4:
                    return 4
                
                case 5:
                    return 5
                
                case _:
                    print("invalid input!!! please try again")
                    press_enter()

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

            choice = input("Are you sure you want to exit? (y/n): ").lower()

            if choice == "y":
                return True

            elif choice == "n":
                return False

            else:
                print("Invalid Input!")

            




