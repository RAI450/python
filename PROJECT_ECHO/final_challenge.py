from puzzle import Puzzle
from utils import press_enter, print_header
from data import (
    FINAL_PUZZLE1, FINAL_ANSWER1, FINAL_HINT1,
    FINAL_PUZZLE2, FINAL_ANSWER2, FINAL_HINT2,
    FINAL_PUZZLE3, FINAL_ANSWER3, FINAL_HINT3,
)


class FinalChallenge:

    def __init__(self):
        self.puzzle1 = Puzzle(FINAL_PUZZLE1, FINAL_ANSWER1, FINAL_HINT1)
        self.puzzle2 = Puzzle(FINAL_PUZZLE2, FINAL_ANSWER2, FINAL_HINT2)
        self.puzzle3 = Puzzle(FINAL_PUZZLE3, FINAL_ANSWER3, FINAL_HINT3)

    def start(self, player):
        """Run all three shutdown puzzles in sequence.

        Returns:
            True        -- all three puzzles solved, shutdown authorized
            False       -- player backed out of a puzzle without solving it
            "GAME_OVER" -- player's health reached 0 during a puzzle
        """

        print_header("Final Shutdown Sequence")

        print("""PROJECT ECHO has locked the Command Center.
Three security authentications are required.
Complete all challenges to activate
the Emergency Shutdown.
""")

        press_enter()

        for level, puzzle in enumerate(
            (self.puzzle1, self.puzzle2, self.puzzle3), start=1
        ):
            print_header(f"Level {level}")

            puzzle.start(player)

            if puzzle.fatal:
                return "GAME_OVER"

            if not puzzle.solved:
                return False

            print(f"\nAuthentication Level {level} Complete.\n")
            press_enter()

        print("""
Authentication Complete.

Emergency Shutdown Authorized.
""")

        press_enter()

        return True
