from utils import press_enter, print_header, print_divider, get_int_choice
from item import Item

PUZZLE_BONUS_SCORE = 20
PERFECT_SOLVE_BONUS = 10  # extra score for solving with zero wrong attempts


class Room:

    def __init__(self, name, description, puzzle=None, reward=None, evidence=None,
                 next_room=None, look_items=None, required_access=0):
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
        print_header(self.name)
        print(self.description)
        press_enter()

    def show_room_menu(self, player):

        while True:
            print(f"""
{'-' * 20} {self.name} {'-' * 20}

                1. Look Around
                2. Solve Puzzle
                3. Collect Reward
                4. Read Evidence
                5. Move Forward

                6. View Player Profile
                7. View Backpack
                8. View Evidence Collection
                9. Back to Game Menu
""")
            print_divider()

            choice = input("Enter your choice : ").strip()

            match choice:

                case "1":
                    self.look_around()

                case "2":
                    result = self.solve_puzzle(player)

                    if result == "GAME_OVER":
                        return "GAME_OVER"

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

                case "8":
                    player.show_evidence()
                    press_enter()

                case "9":
                    return "BACK"

                case _:
                    print("Invalid Choice!")

    def look_around(self):

        if not self.look_items:
            print("Nothing interesting here.")
            press_enter()
            return

        while True:
            print_header(self.name)

            count = 1
            for item_name in self.look_items:
                print(f"{count}. {item_name}")
                count += 1

            print(f"{count}. Go Back")

            choice = get_int_choice("\nEnter choice : ", 1, count)

            if choice == count:
                break

            key = list(self.look_items.keys())[choice - 1]
            print(self.look_items[key])
            press_enter()

    def solve_puzzle(self, player):

        if self.puzzle_solved:
            print("""
    You have already solved this puzzle.
    """)
            press_enter()
            return None

        if self.puzzle is None:
            print("No puzzle in this room.")
            press_enter()
            return None

        self.puzzle.start(player)

        if self.puzzle.fatal:
            return "GAME_OVER"

        if self.puzzle.solved:

            self.puzzle_solved = True

            score_gained = PUZZLE_BONUS_SCORE

            if self.puzzle.wrong_attempts == 0:
                score_gained += PERFECT_SOLVE_BONUS

            player.add_score(score_gained)

            print_header("Puzzle Solved")

            if self.puzzle.wrong_attempts == 0:
                print(f"      Flawless solve! +{score_gained} Score\n")
            else:
                print(f"      +{score_gained} Score\n")

            press_enter()

        return None

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

        reward_item = Item(
            name=self.reward,
            description=f"Recovered from the {self.name}. Grants access to the next restricted area.",
            usable=True
        )

        player.add_item(reward_item)
        player.increase_access_level()

        print_header("Reward Collected")

        print(f"""            You collected:

            {self.reward}

            Access Level Increased!

            Current Access Level : {player.access_level}
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
