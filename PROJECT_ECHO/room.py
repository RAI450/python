from utils import press_enter


class Room:

    def __init__(self, name, description, puzzle=None, reward=None, evidence=None, next_room=None, look_items=None,required_access=0):
        self.name = name
        self.description = description
        self.puzzle = puzzle
        self.reward = reward
        self.evidence = evidence
        self.next_room = next_room
        self.puzzle_solved = False
        self.look_items = look_items
        self.required_access = required_access

    def enter(self):
        print(f"""
============================================================
                  {self.name.upper()}
============================================================

{self.description}
""")

        press_enter()

    def show_room_menu(self,player):

        while True:

            print(f"""
-------------------- {self.name} --------------------

                1. Look Around
                2. Solve Puzzle
                3. Collect Reward
                4. Read Evidence
                5. Move Forward

                6. View Player Profile
                7. View Backpack
                8. View Evidence Collection
                9. Back to Game Menu
--------------------------------------------------------

""")

            choice = input("Enter your choice : ")

            match choice:

                case "1":
                    self.look_around()

                case "2":
                    self.solve_puzzle(player)

                case "3":
                    self.collect_reward(player)

                case "4":
                    self.read_evidence(player)

                case "5":

                    if not self.puzzle_solved:

                        print("""
                The security door is locked.
                Solve the puzzle first.
                """)

                        press_enter()

                    elif player.access_level < self.required_access + 1:

                        print("""
                ACCESS DENIED

                You need a higher access level.
                Collect the room reward first.
                """)

                        press_enter()

                    else:

                        return "NEXT"
                    

                case "6":
                    player.show_player_info()

                    press_enter()

                case "7":
                    player.show_backpack()

                    press_enter()
                
                case "8":
                    player.show_evidence()

                    press_enter()

                case "9":
                    return "BACK"

                case _:
                    print("Invalid Choice!")


    def look_around(self):

        if self.look_items is None:
            print("Nothing interesting here.")
            press_enter()
            return

        while True:

            print(f"""
    ------------ {self.name.upper()} -----------
    """)

            count = 1

            for item in self.look_items:
                print(f"{count}. {item}")

                count += 1

            print(f"{count}. Go Back")

            choice = input("\nEnter choice : ")

            if choice.isdigit():

                choice = int(choice)

                if 1 <= choice <= len(self.look_items):

                    key = list(self.look_items.keys())[choice - 1]

                    print(self.look_items[key])

                    press_enter()

                elif choice == len(self.look_items) + 1:

                    break

                else:

                    print("Invalid Choice.")

            else:

                print("Invalid Choice.")

    def solve_puzzle(self, player):

        if self.puzzle_solved:
            print("""
    You have already solved this puzzle.
    """)
            press_enter()
            return

        if self.puzzle is None:
            print("No puzzle in this room.")
            press_enter()
            return

        self.puzzle.start()

        if self.puzzle.solved:

            self.puzzle_solved = True

            player.add_score(20)

            print("""
    ==========================================

                Puzzle Solved!

                  +20 Score

    ==========================================
    """)

            press_enter()      

    def collect_reward(self, player):

        if not self.puzzle_solved:
            print("""
    You must solve the room puzzle first.

    The reward is locked.
    """)
            press_enter()
            return

        if self.reward is None:
            print("Reward already collected.")
            press_enter()
            return

        player.add_item(self.reward)
        player.increase_access_level()

        print(f"""
    ==========================================

            You collected:

            {self.reward}

            Access Level Increased!

            Current Access Level : {player.access_level}

    -------------------------------------------
    """)

        self.reward = None

        press_enter()

    def read_evidence(self, player):

        if self.evidence is None:
            print("No evidence found.")
            press_enter()
            return

        if self.evidence.title not in player.evidence_list:
            player.add_evidence(self.evidence.title)

        self.evidence.display()

        press_enter()