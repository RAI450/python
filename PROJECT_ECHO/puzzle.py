from utils import press_enter, print_header

WRONG_ANSWER_DAMAGE = 10


class Puzzle:

    def __init__(self, question, answer, hint):
        self.question = question
        self.answer = answer
        self.hint = hint
        self.solved = False
        self.wrong_attempts = 0
        self.fatal = False  # True if the player's health hit 0 here

    def start(self, player=None):
        """Run the puzzle loop. If a player is passed in, wrong answers
        cost health -- matching what the instructions screen promises.
        If health reaches 0, self.fatal is set to True and the loop
        ends immediately so the caller can trigger Game Over."""

        while True:
            print_header("Puzzle")
            print(self.question)

            print("""
1. Answer
2. Hint
3. Exit Puzzle
""")

            choice = input("Enter choice : ").strip()

            match choice:

                case "1":
                    user_answer = input("Your Answer : ").strip().lower()

                    if user_answer == self.answer.strip().lower():
                        print("""
Correct!

Puzzle Solved.
""")
                        self.solved = True
                        press_enter()
                        break

                    else:
                        self.wrong_attempts += 1

                        if player is not None:
                            alive = player.take_damage(WRONG_ANSWER_DAMAGE)

                            print(f"""
Wrong Answer. Try Again.

You take {WRONG_ANSWER_DAMAGE} damage. (Health: {player.health}/100)
""")

                            if not alive:
                                print("""
Your health has reached 0.

You collapse...
""")
                                self.fatal = True
                                press_enter()
                                return

                        else:
                            print("""
Wrong Answer.
Try Again.
""")

                        press_enter()

                case "2":
                    print(f"""
Hint :

{self.hint}
""")
                    press_enter()

                case "3":
                    break

                case _:
                    print("Invalid Choice!")
                    press_enter()
