from utils import press_enter


class Puzzle:

    def __init__(self, question, answer, hint):
        self.question = question
        self.answer = answer
        self.hint = hint
        self.solved = False

    def start(self):

        while True:

            print("""
================ PUZZLE ================
""")

            print(self.question)

            print("""
1. Answer
2. Hint
3. Exit Puzzle
""")

            choice = input("Enter choice : ")

            match choice:

                case "1":

                    user_answer = input("Your Answer : ")

                    if user_answer.lower() == self.answer.lower():

                        print("""
Correct!

Puzzle Solved.
""")

                        self.solved = True

                        press_enter()

                        break

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