from puzzle import Puzzle
from utils import press_enter
from data import *

class FinalChallenge:

    def __init__(self):

        self.puzzle1 = Puzzle(
            FINAL_PUZZLE1,
            FINAL_ANSWER1,
            FINAL_HINT1
        )

        self.puzzle2 = Puzzle(
            FINAL_PUZZLE2,
            FINAL_ANSWER2,
            FINAL_HINT2
        )

        self.puzzle3 = Puzzle(
            FINAL_PUZZLE3,
            FINAL_ANSWER3,
            FINAL_HINT3
        )

    def start(self):

        print("""
==================================================
            FINAL SHUTDOWN SEQUENCE
==================================================

PROJECT ECHO has locked the Command Center.

Three security authentications are required.

Complete all challenges to activate
the Emergency Shutdown.

==================================================
""")

        press_enter()

        # ---------------- Puzzle 1 ----------------

        print("""
================ LEVEL 1 =================
""")

        self.puzzle1.start()

        if not self.puzzle1.solved:
            return False

        print("""
Authentication Level 1 Complete.
""")

        press_enter()

        # ---------------- Puzzle 2 ----------------

        print("""
================ LEVEL 2 =================
""")

        self.puzzle2.start()

        if not self.puzzle2.solved:
            return False

        print("""
Authentication Level 2 Complete.
""")

        press_enter()

        # ---------------- Puzzle 3 ----------------

        print("""
================ LEVEL 3 =================
""")

        self.puzzle3.start()

        if not self.puzzle3.solved:
            return False

        print("""
Authentication Complete.

Emergency Shutdown Authorized.
""")

        press_enter()

        return True