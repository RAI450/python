from menu import Menu
from utils import press_enter, print_header, progress_bar
from player import Player
from room import Room
from puzzle import Puzzle
from evidence import Evidence
from final_challenge import FinalChallenge

import time

from data import (
    story2,

    RECEPTION_NAME,
    RECEPTION_DESCRIPTION,
    RECEPTION_PUZZLE_QUESTION,
    RECEPTION_PUZZLE_ANSWER,
    RECEPTION_PUZZLE_HINT,
    RECEPTION_EVIDENCE_TITLE,
    RECEPTION_EVIDENCE_CONTENT,
    RECEPTION_REWARD,
    RECEPTION_DESK,
    RECEPTION_COMPUTER,
    RECEPTION_WAITING_AREA,
    RECEPTION_NOTICE_BOARD,

    SECURITY_NAME,
    SECURITY_DESCRIPTION,
    SECURITY_PUZZLE_QUESTION,
    SECURITY_PUZZLE_ANSWER,
    SECURITY_PUZZLE_HINT,
    SECURITY_EVIDENCE_TITLE,
    SECURITY_EVIDENCE_CONTENT,
    SECURITY_REWARD,
    SECURITY_CCTV,
    SECURITY_LOCKER,
    SECURITY_WEAPON_CABINET,
    SECURITY_MASTER_COMPUTER,

    MEDICAL_NAME,
    MEDICAL_DESCRIPTION,
    MEDICAL_BED,
    MEDICAL_CABINET,
    MEDICAL_COMPUTER,
    MEDICAL_OPERATION_ROOM,
    MEDICAL_PUZZLE_QUESTION,
    MEDICAL_PUZZLE_ANSWER,
    MEDICAL_PUZZLE_HINT,
    MEDICAL_EVIDENCE_TITLE,
    MEDICAL_EVIDENCE_CONTENT,
    MEDICAL_REWARD,

    STORAGE_NAME,
    STORAGE_DESCRIPTION,
    STORAGE_BOXES,
    STORAGE_SHELVES,
    STORAGE_TOOLBOX,
    STORAGE_VENT,
    STORAGE_PUZZLE_QUESTION,
    STORAGE_PUZZLE_ANSWER,
    STORAGE_PUZZLE_HINT,
    STORAGE_EVIDENCE_TITLE,
    STORAGE_EVIDENCE_CONTENT,
    STORAGE_REWARD,

    LAB_NAME,
    LAB_DESCRIPTION,
    LAB_WORKSTATION,
    LAB_EXPERIMENT,
    LAB_WHITEBOARD,
    LAB_COMPUTER,
    LAB_PUZZLE_QUESTION,
    LAB_PUZZLE_ANSWER,
    LAB_PUZZLE_HINT,
    LAB_EVIDENCE_TITLE,
    LAB_EVIDENCE_CONTENT,
    LAB_REWARD,

    SERVER_NAME,
    SERVER_DESCRIPTION,
    SERVER_MAINFRAME,
    SERVER_RACKS,
    SERVER_MONITOR,
    SERVER_BACKUP,
    SERVER_PUZZLE_QUESTION,
    SERVER_PUZZLE_ANSWER,
    SERVER_PUZZLE_HINT,
    SERVER_EVIDENCE_TITLE,
    SERVER_EVIDENCE_CONTENT,
    SERVER_REWARD,

    REACTOR_NAME,
    REACTOR_DESCRIPTION,
    REACTOR_CORE,
    REACTOR_CONTROL_PANEL,
    REACTOR_COOLING_SYSTEM,
    REACTOR_OBSERVATION_WINDOW,
    REACTOR_PUZZLE_QUESTION,
    REACTOR_PUZZLE_ANSWER,
    REACTOR_PUZZLE_HINT,
    REACTOR_EVIDENCE_TITLE,
    REACTOR_EVIDENCE_CONTENT,
    REACTOR_REWARD,

    COMMAND_NAME,
    COMMAND_DESCRIPTION,
    COMMAND_AI_CORE,
    COMMAND_MAIN_CONSOLE,
    COMMAND_MONITORS,
    COMMAND_WINDOW,
    COMMAND_EVIDENCE_TITLE,
    COMMAND_EVIDENCE_CONTENT,

)

# Current room's display name -> what the player is trying to achieve there.
ROOM_OBJECTIVES = {
    "Reception Hall": "Find the Reception Key Card.",
    "Security Office": "Restore Security Access.",
    "Medical Bay": "Restore Medical Department Access.",
    "Storage Room": "Search the storage area and obtain the Storage Key Card.",
    "Research Laboratory": "Search your father's laboratory and uncover the truth.",
    "Server Room": "Disable the Facility AI and locate the Reactor Core.",
    "Reactor Core": "Stabilize the reactor and reach the Command Center.",
    "Command Center": "Activate the Emergency Shutdown and stop PROJECT ECHO.",
}


class Game:

    def __init__(self):

        self.menu = Menu()
        self.player = None
        self.current_room = None
        self.rooms = []
        self.game_running = True

    # ======================================================

    def start_game(self):

        self.loading_screen()
        self.title_screen()

        while self.game_running:

            choice = self.menu.show_main_menu()

            match choice:

                case 1:
                    self.new_game()

                case 2:
                    self.menu.show_story()

                case 3:
                    self.menu.show_instructions()

                case 4:
                    self.menu.show_credits()

                case 5:

                    if self.menu.confirm_exit():
                        self.end_game()

    # ======================================================

    def loading_screen(self):

        print("""
    =====================================================
                    PROJECT ECHO
    =====================================================
    """)

        print("Loading Game...\n")

        for i in [0, 10, 20, 35, 50, 65, 80, 90, 100]:
            print(f"Loading {progress_bar(i, 100)}")
            time.sleep(0.3)

        print("\nGame Loaded Successfully!")

        press_enter()

    # ======================================================

    def title_screen(self):

        print("""
        ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
        ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
        ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║
        ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║
        ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║
        ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝

                ███████╗ ██████╗██╗  ██╗ ██████╗
                ██╔════╝██╔════╝██║  ██║██╔═══██╗
                █████╗  ██║     ███████║██║   ██║
                ██╔══╝  ██║     ██╔══██║██║   ██║
                ███████╗╚██████╗██║  ██║╚██████╔╝
                ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝
    """)

        print("""
    ========================================================

                SOME EXPERIMENTS SHOULD NEVER
                    HAVE BEEN COMPLETED!!!

                        Version 1.0

                  Developed By SAHIL RAI

    ========================================================
    """)

        press_enter()

    # ======================================================

    def new_game(self):

        print_header("New Game")

        name = ""

        while not name:
            name = input("Enter your name : ").strip()

            if not name:
                print("Name cannot be empty. Please try again.\n")

        self.player = Player(name)

        print(f"""

                Welcome, {name}

                Initializing Player Profile...

                Loading Mission...

""")

        press_enter()

        self.player.show_player_info()

        press_enter()

        story2(name)

        press_enter()

        self.create_rooms()

        self.start_rooms()

    # ======================================================

    def _build_room(self, name, description, puzzle_data, reward,
                     evidence_data, look_items, required_access):
        """Assemble one Room together with its Puzzle and Evidence.

        Every room used to repeat the same three or four lines to build
        its Puzzle and Evidence objects before creating the Room. This
        helper keeps that logic in one place instead of copy-pasted
        eight times.
        """

        puzzle = Puzzle(*puzzle_data) if puzzle_data else None
        evidence = Evidence(*evidence_data) if evidence_data else None

        return Room(
            name,
            description,
            puzzle,
            reward,
            evidence,
            look_items=look_items,
            required_access=required_access
        )

    def create_rooms(self):

        reception_room = self._build_room(
            RECEPTION_NAME, RECEPTION_DESCRIPTION,
            (RECEPTION_PUZZLE_QUESTION, RECEPTION_PUZZLE_ANSWER, RECEPTION_PUZZLE_HINT),
            RECEPTION_REWARD,
            (RECEPTION_EVIDENCE_TITLE, RECEPTION_EVIDENCE_CONTENT),
            look_items={
                "Reception Desk": RECEPTION_DESK,
                "Broken Computer": RECEPTION_COMPUTER,
                "Waiting Area": RECEPTION_WAITING_AREA,
                "Notice Board": RECEPTION_NOTICE_BOARD
            },
            required_access=0
        )

        security_room = self._build_room(
            SECURITY_NAME, SECURITY_DESCRIPTION,
            (SECURITY_PUZZLE_QUESTION, SECURITY_PUZZLE_ANSWER, SECURITY_PUZZLE_HINT),
            SECURITY_REWARD,
            (SECURITY_EVIDENCE_TITLE, SECURITY_EVIDENCE_CONTENT),
            look_items={
                "CCTV Monitor": SECURITY_CCTV,
                "Security Locker": SECURITY_LOCKER,
                "Weapon Cabinet": SECURITY_WEAPON_CABINET,
                "Master Computer": SECURITY_MASTER_COMPUTER
            },
            required_access=1
        )

        medical_room = self._build_room(
            MEDICAL_NAME, MEDICAL_DESCRIPTION,
            (MEDICAL_PUZZLE_QUESTION, MEDICAL_PUZZLE_ANSWER, MEDICAL_PUZZLE_HINT),
            MEDICAL_REWARD,
            (MEDICAL_EVIDENCE_TITLE, MEDICAL_EVIDENCE_CONTENT),
            look_items={
                "Hospital Bed": MEDICAL_BED,
                "Medicine Cabinet": MEDICAL_CABINET,
                "Medical Computer": MEDICAL_COMPUTER,
                "Operating Room Door": MEDICAL_OPERATION_ROOM
            },
            required_access=2
        )

        storage_room = self._build_room(
            STORAGE_NAME, STORAGE_DESCRIPTION,
            (STORAGE_PUZZLE_QUESTION, STORAGE_PUZZLE_ANSWER, STORAGE_PUZZLE_HINT),
            STORAGE_REWARD,
            (STORAGE_EVIDENCE_TITLE, STORAGE_EVIDENCE_CONTENT),
            look_items={
                "Supply Boxes": STORAGE_BOXES,
                "Metal Shelves": STORAGE_SHELVES,
                "Tool Box": STORAGE_TOOLBOX,
                "Ventilation Duct": STORAGE_VENT
            },
            required_access=3
        )

        lab_room = self._build_room(
            LAB_NAME, LAB_DESCRIPTION,
            (LAB_PUZZLE_QUESTION, LAB_PUZZLE_ANSWER, LAB_PUZZLE_HINT),
            LAB_REWARD,
            (LAB_EVIDENCE_TITLE, LAB_EVIDENCE_CONTENT),
            look_items={
                "Father's Workstation": LAB_WORKSTATION,
                "Experiment Chamber": LAB_EXPERIMENT,
                "Whiteboard": LAB_WHITEBOARD,
                "Research Computer": LAB_COMPUTER
            },
            required_access=4
        )

        server_room = self._build_room(
            SERVER_NAME, SERVER_DESCRIPTION,
            (SERVER_PUZZLE_QUESTION, SERVER_PUZZLE_ANSWER, SERVER_PUZZLE_HINT),
            SERVER_REWARD,
            (SERVER_EVIDENCE_TITLE, SERVER_EVIDENCE_CONTENT),
            look_items={
                "Central Mainframe": SERVER_MAINFRAME,
                "Server Racks": SERVER_RACKS,
                "Security Monitor": SERVER_MONITOR,
                "Backup Generator": SERVER_BACKUP
            },
            required_access=5
        )

        reactor_room = self._build_room(
            REACTOR_NAME, REACTOR_DESCRIPTION,
            (REACTOR_PUZZLE_QUESTION, REACTOR_PUZZLE_ANSWER, REACTOR_PUZZLE_HINT),
            REACTOR_REWARD,
            (REACTOR_EVIDENCE_TITLE, REACTOR_EVIDENCE_CONTENT),
            look_items={
                "Reactor Core": REACTOR_CORE,
                "Control Panel": REACTOR_CONTROL_PANEL,
                "Cooling System": REACTOR_COOLING_SYSTEM,
                "Observation Window": REACTOR_OBSERVATION_WINDOW
            },
            required_access=6
        )

        command_room = self._build_room(
            COMMAND_NAME, COMMAND_DESCRIPTION,
            puzzle_data=None,
            reward=None,
            evidence_data=(COMMAND_EVIDENCE_TITLE, COMMAND_EVIDENCE_CONTENT),
            look_items={
                "AI Core": COMMAND_AI_CORE,
                "Main Console": COMMAND_MAIN_CONSOLE,
                "Security Monitors": COMMAND_MONITORS,
                "Observation Window": COMMAND_WINDOW
            },
            required_access=7
        )

        # ---------------- Connect Rooms ----------------

        reception_room.next_room = security_room
        security_room.next_room = medical_room
        medical_room.next_room = storage_room
        storage_room.next_room = lab_room
        lab_room.next_room = server_room
        server_room.next_room = reactor_room
        reactor_room.next_room = command_room

        # ---------------- Store Rooms ----------------

        self.rooms = [
            reception_room,
            security_room,
            medical_room,
            storage_room,
            lab_room,
            server_room,
            reactor_room,
            command_room,
        ]

        self.current_room = reception_room

    # ======================================================

    def start_rooms(self):

        room_number = 1

        while self.current_room is not None:

            print_header(f"Room {room_number} / {len(self.rooms)}")

            self.player.show_hud()

            press_enter()

            self.show_objective()

            press_enter()

            self.current_room.enter()

            # ---------------- FINAL ROOM ----------------

            if self.current_room.name == "Command Center":

                self.current_room.read_evidence(self.player)

                challenge = FinalChallenge()

                result = challenge.start(self.player)

                if result == "GAME_OVER":
                    self.game_over()
                    return

                if result:
                    self.ending()
                    return

                print("""
    Emergency Shutdown Failed.

    Returning to Command Center...
    """)

                press_enter()

                continue

            # ---------------- NORMAL ROOMS ----------------

            action = self.current_room.show_room_menu(self.player)

            if action == "GAME_OVER":

                self.game_over()

                return

            elif action == "NEXT":

                self.current_room = self.current_room.next_room

                room_number += 1

            elif action == "BACK":
                break

    # ======================================================

    def game_over(self):

        print_header("Game Over")

        print(f"""
{self.player.name}, your injuries were too severe to continue.

PROJECT ECHO claims another victim...

------------------------------------------------------------
                  FINAL STATISTICS
------------------------------------------------------------
            Score           : {self.player.score}
            Evidence Found  : {len(self.player.evidence_list)} / 8
            Access Level    : {self.player.access_level}
------------------------------------------------------------

You can start a New Game from the Main Menu to try again.
""")

        press_enter()

    # ======================================================

    def ending(self):

        print_header("Emergency Shutdown")

        input("Press Enter to begin shutdown...")

        progress = [10, 30, 55, 70, 95, 100]

        for value in progress:
            print(f"Shutdown Progress : {progress_bar(value, 100)}")
            time.sleep(0.2)

        print("""
    PROJECT ECHO:

    "No...

    This is impossible..."

    Signal Lost.
    """)

        press_enter()

        print_header("Reactor Failure Detected")

        print("""
    WARNING!

    SELF DESTRUCTION ACTIVATED!
    """)

        press_enter()

        for i in range(10, 0, -1):
            print(i)
            time.sleep(0.15)

        print("""
    You sprint toward the emergency exit...

    The massive blast door slowly opens.

    Fresh sunlight fills the corridor.

    You escape the facility just in time...
    """)

        press_enter()

        print("""
    BOOOOOOOOOOOOOOOOOM!!!!!

    A massive explosion destroys
    the Helix Research Facility.

    PROJECT ECHO has been destroyed forever.
    """)

        press_enter()

        print_header("Mission Complete")

        print("""
    Congratulations!

    You completed PROJECT ECHO.

    Your father's mission has finally ended.
    """)

        press_enter()

        self.show_final_stats()

        print_header("Credits")

        print("""
                         PROJECT ECHO
                    Developed By - SAHIL RAI
                         Version 1.0

                    Thank you for playing!
    """)

        press_enter()

        self.end_game()

    # ======================================================

    def show_final_stats(self):

        print_header("Mission Summary")

        print(f"""
            Agent            : {self.player.name}
            Final Score      : {self.player.score}
            Evidence Found   : {len(self.player.evidence_list)} / 8
            Items Collected  : {len(self.player.backpack.items)}
            Health Remaining : {self.player.health} / 100
""")

        press_enter()

    # ======================================================

    def show_objective(self):

        objective = ROOM_OBJECTIVES.get(self.current_room.name, "Explore the room.")

        print_header("Current Objective")

        print(f"        ► {objective}\n")

    # ======================================================

    def end_game(self):

        print("""
########################################################

                PROJECT ECHO

                 COMPLETED

########################################################
""")

        print("""

Thank you for playing PROJECT ECHO.

Goodbye!

""")

        self.game_running = False
