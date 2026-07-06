from menu import Menu
from utils import press_enter
from player import Player
from room import Room
from puzzle import Puzzle
from evidence import Evidence
from final_challenge import FinalChallenge

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

        print("Loading PROJECT ECHO...")
        print("Please wait...\n")

    # ======================================================

    def title_screen(self):

        print("""
############################################################
                    PROJECT ECHO
############################################################

Some experiments should never have been completed.

Version 1.0

Developed By : Sahil Rai
""")

    # ======================================================

    def new_game(self):

        print("""
==========================================================
                        NEW GAME
==========================================================
""")

        name = input("Enter your name : ")

        self.player = Player(name)

        print(f"""

Welcome, {name}!

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

    def create_rooms(self):

        # ---------------- Reception ----------------

        reception_puzzle = Puzzle(
            RECEPTION_PUZZLE_QUESTION,
            RECEPTION_PUZZLE_ANSWER,
            RECEPTION_PUZZLE_HINT
        )

        reception_evidence = Evidence(
            RECEPTION_EVIDENCE_TITLE,
            RECEPTION_EVIDENCE_CONTENT
        )

        reception_room = Room(
            RECEPTION_NAME,
            RECEPTION_DESCRIPTION,
            reception_puzzle,
            RECEPTION_REWARD,
            reception_evidence,
            look_items={
                "Reception Desk": RECEPTION_DESK,
                "Broken Computer": RECEPTION_COMPUTER,
                "Waiting Area": RECEPTION_WAITING_AREA,
                "Notice Board": RECEPTION_NOTICE_BOARD
            },
            required_access=0
        )

        # ---------------- Security ----------------

        security_puzzle = Puzzle(
            SECURITY_PUZZLE_QUESTION,
            SECURITY_PUZZLE_ANSWER,
            SECURITY_PUZZLE_HINT
        )

        security_evidence = Evidence(
            SECURITY_EVIDENCE_TITLE,
            SECURITY_EVIDENCE_CONTENT
        )

        security_room = Room(
            SECURITY_NAME,
            SECURITY_DESCRIPTION,
            security_puzzle,
            SECURITY_REWARD,
            security_evidence,
            look_items={
                "CCTV Monitor": SECURITY_CCTV,
                "Security Locker": SECURITY_LOCKER,
                "Weapon Cabinet": SECURITY_WEAPON_CABINET,
                "Master Computer": SECURITY_MASTER_COMPUTER
            },
            required_access=1
        )
        # ---------------- Medical Bay ----------------

        medical_puzzle = Puzzle(
            MEDICAL_PUZZLE_QUESTION,
            MEDICAL_PUZZLE_ANSWER,
            MEDICAL_PUZZLE_HINT
        )

        medical_evidence = Evidence(
            MEDICAL_EVIDENCE_TITLE,
            MEDICAL_EVIDENCE_CONTENT
        )

        medical_room = Room(
            MEDICAL_NAME,
            MEDICAL_DESCRIPTION,
            medical_puzzle,
            MEDICAL_REWARD,
            medical_evidence,
            look_items={
                "Hospital Bed": MEDICAL_BED,
                "Medicine Cabinet": MEDICAL_CABINET,
                "Medical Computer": MEDICAL_COMPUTER,
                "Operating Room Door": MEDICAL_OPERATION_ROOM
            },
            required_access=2
        )

        # ---------------- Storage Room ----------------

        storage_puzzle = Puzzle(
            STORAGE_PUZZLE_QUESTION,
            STORAGE_PUZZLE_ANSWER,
            STORAGE_PUZZLE_HINT
        )

        storage_evidence = Evidence(
            STORAGE_EVIDENCE_TITLE,
            STORAGE_EVIDENCE_CONTENT
        )

        storage_room = Room(
            STORAGE_NAME,
            STORAGE_DESCRIPTION,
            storage_puzzle,
            STORAGE_REWARD,
            storage_evidence,
            look_items={
                "Supply Boxes": STORAGE_BOXES,
                "Metal Shelves": STORAGE_SHELVES,
                "Tool Box": STORAGE_TOOLBOX,
                "Ventilation Duct": STORAGE_VENT
            },
            required_access=3
        )
        # ---------------- Research Laboratory ----------------

        lab_puzzle = Puzzle(
            LAB_PUZZLE_QUESTION,
            LAB_PUZZLE_ANSWER,
            LAB_PUZZLE_HINT
        )

        lab_evidence = Evidence(
            LAB_EVIDENCE_TITLE,
            LAB_EVIDENCE_CONTENT
        )

        lab_room = Room(
            LAB_NAME,
            LAB_DESCRIPTION,
            lab_puzzle,
            LAB_REWARD,
            lab_evidence,
            look_items={
                "Father's Workstation": LAB_WORKSTATION,
                "Experiment Chamber": LAB_EXPERIMENT,
                "Whiteboard": LAB_WHITEBOARD,
                "Research Computer": LAB_COMPUTER
            },
            required_access=4
        )

        # ---------------- Server Room ----------------

        server_puzzle = Puzzle(
            SERVER_PUZZLE_QUESTION,
            SERVER_PUZZLE_ANSWER,
            SERVER_PUZZLE_HINT
        )

        server_evidence = Evidence(
            SERVER_EVIDENCE_TITLE,
            SERVER_EVIDENCE_CONTENT
        )

        server_room = Room(
            SERVER_NAME,
            SERVER_DESCRIPTION,
            server_puzzle,
            SERVER_REWARD,
            server_evidence,
            look_items={
                "Central Mainframe": SERVER_MAINFRAME,
                "Server Racks": SERVER_RACKS,
                "Security Monitor": SERVER_MONITOR,
                "Backup Generator": SERVER_BACKUP
            },
            required_access=5
        )
        # ---------------- Reactor Core ----------------

        reactor_puzzle = Puzzle(
            REACTOR_PUZZLE_QUESTION,
            REACTOR_PUZZLE_ANSWER,
            REACTOR_PUZZLE_HINT
        )

        reactor_evidence = Evidence(
            REACTOR_EVIDENCE_TITLE,
            REACTOR_EVIDENCE_CONTENT
        )

        reactor_room = Room(
            REACTOR_NAME,
            REACTOR_DESCRIPTION,
            reactor_puzzle,
            REACTOR_REWARD,
            reactor_evidence,
            look_items={
                "Reactor Core": REACTOR_CORE,
                "Control Panel": REACTOR_CONTROL_PANEL,
                "Cooling System": REACTOR_COOLING_SYSTEM,
                "Observation Window": REACTOR_OBSERVATION_WINDOW
            },
            required_access=6
        )
        # ---------------- Command Center ----------------

        command_evidence = Evidence(
            COMMAND_EVIDENCE_TITLE,
            COMMAND_EVIDENCE_CONTENT
        )

        command_room = Room(
            COMMAND_NAME,
            COMMAND_DESCRIPTION,
            puzzle=None,
            reward=None,
            evidence=command_evidence,
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

        self.rooms.append(reception_room)
        self.rooms.append(security_room)
        self.rooms.append(medical_room)
        self.rooms.append(storage_room)
        self.rooms.append(lab_room)
        self.rooms.append(server_room)
        self.rooms.append(reactor_room)
        self.rooms.append(command_room)

        self.current_room = reception_room

    def start_rooms(self):

        room_number = 1

        while self.current_room is not None:

            print(f"""
    ================================================
                ROOM {room_number} / {len(self.rooms)}
    ================================================
    """)

            self.player.show_hud()

            self.show_objective()

            self.current_room.enter()

            # ---------------- FINAL ROOM ----------------

            if self.current_room.name == "Command Center":

                self.current_room.read_evidence(self.player)

                challenge = FinalChallenge()

                if challenge.start():

                    self.ending()

                    return

                else:

                    print("""
    Emergency Shutdown Failed.

    Returning to Command Center...
    """)

                    press_enter()

                    continue

            # ---------------- NORMAL ROOMS ----------------

            action = self.current_room.show_room_menu(self.player)

            if action == "NEXT":

                self.current_room = self.current_room.next_room

                room_number += 1

            elif action == "BACK":

                break
    def ending(self):

        print("""
    ========================================================
                EMERGENCY SHUTDOWN
    ========================================================
    """)

        input("Press Enter to begin shutdown...")

        progress = [10, 30, 55, 70, 95, 100]

        for value in progress:

            print(f"Shutdown Progress : {value}%")

        print("""
    PROJECT ECHO:

    "No...

    This is impossible..."

    Signal Lost.
    """)

        press_enter()

        print("""
    ========================================================
            REACTOR FAILURE DETECTED
    ========================================================

    WARNING!

    SELF DESTRUCTION ACTIVATED!
    """)

        press_enter()

        for i in range(10, 0, -1):

            print(i)

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

        print("""
    ========================================================
                    MISSION COMPLETE
    ========================================================

    Congratulations!

    You completed PROJECT ECHO.

    Your father's mission has finally ended.
    """)

        press_enter()

        print("""
    ========================================================
                        CREDITS
    ========================================================

    PROJECT ECHO

    Developed By

    SAHIL RAI

    Python OOP Project

    Version 1.0

    Thank you for playing!

    ========================================================
    """)

        press_enter()

        self.end_game()

    def show_objective(self):

        objectives = {

            "Reception Hall":
            "Find the Reception Key Card.",

            "Security Office":
            "Restore Security Access.",

            "Medical Bay":
            "Restore Medical Department Access.",

            "Storage Room":
            "Search the storage area and obtain the Storage Key Card.",

            "Research Laboratory":
            "Search your father's laboratory and uncover the truth.",

            "Server Room":
            "Disable the Facility AI and locate the Reactor Core.",

            "Reactor Core":
            "Stabilize the reactor and reach the Command Center.",

            "Command Center":
            "Activate the Emergency Shutdown and stop PROJECT ECHO.",

        }

        print("""
    ================================================
                MISSION OBJECTIVE
    ================================================
    """)

        print(objectives.get(self.current_room.name))

        print("""
    ================================================
    """)
# ======================================================================================================
    def end_game(self):

        print("""

Thank you for playing PROJECT ECHO.

Goodbye!

""")

        self.game_running = False