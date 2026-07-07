# ==========================================================
# PROJECT ECHO
# DATA FILE
# Stores:
# Story
# Instructions
# Credits
# Room Descriptions
# Puzzles
# Evidence
# Rewards
# ==========================================================


# ==========================================================
# STORY PART 1
# ==========================================================

def story1():
    print("""
========================= STORY =========================

YEAR: 2048

Deep beneath the mountains, the Helix Research Facility
was built in complete secrecy.

Its purpose was to develop a revolutionary energy source
known only as PROJECT ECHO.

The experiment promised unlimited clean energy for
the entire world.

Then...

One day...

The facility went silent.

Communication stopped.

No scientist ever came out alive.

Governments sealed every record related to PROJECT ECHO.

The incident was classified.

The facility was officially declared abandoned.

No one ever discovered what really happened there.

Among those scientists was...

Dr. Ethan Carter.

Your father.

He was one of the lead scientists working on
PROJECT ECHO.

As a child, you refused to believe he was gone.

For years you searched for answers.

One day you discovered an old map hidden in your home.

The map leads to the abandoned Helix Research Facility.

You decide to uncover the truth about your father.

=========================================================
""")


# ==========================================================
# STORY PART 2
# ==========================================================

def story2(player_name):

    print(f"""
-------------------------------------------------------------
{player_name}...

The entrance of the Helix Research Facility stands before you.

The massive steel gate slowly opens.

You step inside.

...

CLANG!!

The gate slams shut behind you.

Emergency lights begin flashing.

WARNING...

LOCKDOWN PROTOCOL ACTIVATED

POWER FAILURE DETECTED

EMERGENCY EXIT LOCKED

FACILITY SHUTDOWN IN PROGRESS

You are trapped.

The only way out...

is forward.

""")


# ==========================================================
# HOW TO PLAY
# ==========================================================

def instructions():

    print("""
=========================================================
                    HOW TO PLAY
=========================================================

• Explore every room carefully.

• Inspect objects to discover clues.

• Solve puzzles to unlock new areas.

• Collect useful items.

• Gather Evidence Files to reveal the truth.

• Wrong puzzle answers may reduce your health.

• Reach the Emergency Exit to complete the game.

=========================================================
""")


# ==========================================================
# CREDITS
# ==========================================================

def credits():

    print("""
=========================================================
                      PROJECT ECHO
=========================================================

                Developed By ~ Sahil Rai
          
                Python Project(Version 1.0)

                Special Thanks To :-
          
                Ajay Thakur Sir(TRAINER)
          
                ChatGPT (Planning & Mentoring)
          
""")


# ##########################################################
#
# ROOM 1 : RECEPTION HALL
#
# ##########################################################

RECEPTION_NAME = "Reception Hall"

RECEPTION_DESCRIPTION = """
Dust covers every desk.

Broken computers flicker with static.

Employee ID cards are scattered across the floor.

Emergency lights flash red every few seconds.

Somewhere deep inside the facility...

you hear a metallic sound.

You are not alone.
"""
# -------------------- LOOK AROUND --------------------

RECEPTION_DESK = """
You inspect the reception desk.
An old visitor register is still open.
The last visitor signed in at 08:42 AM.
No one ever signed out.
"""

RECEPTION_COMPUTER = """
The computer suddenly powers on.
LOGIN FAILED...
POWER LOSS DETECTED.
A sticky note reads:
'Binary is the key.'
"""

RECEPTION_WAITING_AREA = """
Several chairs are overturned.
Coffee cups remain on the table.
It looks like everyone left in a hurry.
"""

RECEPTION_NOTICE_BOARD = """
A faded notice reads:
PROJECT ECHO
AUTHORIZED PERSONNEL ONLY
LEVEL 3 CLEARANCE REQUIRED
"""

# -------------------- Puzzle --------------------

RECEPTION_PUZZLE_QUESTION = """
A locked terminal asks...

Convert Decimal 10 into Binary.
"""

RECEPTION_PUZZLE_ANSWER = "1010"

RECEPTION_PUZZLE_HINT = """
Think about powers of 2.

8 + 2 = 10
"""

# -------------------- Evidence --------------------

RECEPTION_EVIDENCE_TITLE = "Research Log 001"

RECEPTION_EVIDENCE_CONTENT = """
Project ECHO has entered Phase One.

Energy production has exceeded expectations.

Dr. Ethan Carter believes the reactor
can change the world forever.

However...

Several researchers reported hearing
strange whispers near the Reactor Core.

Management ignored the complaints.
"""

# -------------------- Reward --------------------

RECEPTION_REWARD = "Reception Key Card"


# ##########################################################
#
# ROOM 2 : SECURITY OFFICE
#
# ##########################################################

SECURITY_NAME = "Security Office"

SECURITY_DESCRIPTION = """
Several monitors still display camera feeds.

Most cameras are offline.

One monitor still works.

It shows...

someone walking...

but nobody is actually there.

A security locker is locked.

A master computer waits for authentication.
"""
# -------------------- LOOK AROUND --------------------

SECURITY_CCTV = """
Most camera feeds are offline.

One monitor still works.

For a brief second...

you see a shadow walking
through the hallway.
"""

SECURITY_LOCKER = """
ACCESS DENIED

Security Locker Locked.

Level 1 Access Required.
"""

SECURITY_WEAPON_CABINET = """
The weapon cabinet is empty.

Every weapon has disappeared.
"""

SECURITY_MASTER_COMPUTER = """
SECURITY AUTHENTICATION REQUIRED

Only authorized personnel
may continue.
"""

# -------------------- Puzzle --------------------

SECURITY_PUZZLE_QUESTION = """
Security Authentication

Which Python data structure stores data
using key-value pairs?
"""

SECURITY_PUZZLE_ANSWER = "dictionary"

SECURITY_PUZZLE_HINT = """
Think about collections.

It stores keys and values.
"""

# -------------------- Evidence --------------------

SECURITY_EVIDENCE_TITLE = "Security Report"

SECURITY_EVIDENCE_CONTENT = """
Several scientists attempted
to leave the laboratory.

Emergency doors refused to open.

The Security AI ignored manual commands.

Someone...

or something...

had taken complete control
of the facility.
"""

# -------------------- Reward --------------------

SECURITY_REWARD = "Medical Bay Access Card"

# ##########################################################
#
#                 ROOM 3 : MEDICAL BAY
#
# ##########################################################

MEDICAL_NAME = "Medical Bay"

MEDICAL_DESCRIPTION = """
The air smells strongly of chemicals.

Rows of hospital beds stand empty.

Several beds still have blood stains.

Medical robots remain frozen in place.

One life-support machine suddenly powers off.

A robotic voice echoes...

'Patient... Deceased.'

Silence fills the room.
"""

# -------------------- LOOK AROUND --------------------

MEDICAL_BED = """
One hospital bed is still warm.

Someone was here recently.
"""

MEDICAL_CABINET = """
Most medicines are expired.

One First Aid Kit remains untouched.
"""

MEDICAL_COMPUTER = """
PATIENT DATABASE

Patients : 47

Survivors : 0
"""

MEDICAL_OPERATION_ROOM = """
BIOHAZARD

AUTHORIZED PERSONNEL ONLY
"""

# -------------------- Puzzle --------------------

MEDICAL_PUZZLE_QUESTION = """
Medical Authentication

Which Python data type cannot be changed after creation?
"""

MEDICAL_PUZZLE_ANSWER = "tuple"

MEDICAL_PUZZLE_HINT = """
Lists can change.

This data type cannot.
"""

# -------------------- Evidence --------------------

MEDICAL_EVIDENCE_TITLE = "Research Log 003"

MEDICAL_EVIDENCE_CONTENT = """
Patients complained of hearing voices.

No medical explanation could be found.

Dr. Ethan Carter requested that
PROJECT ECHO be stopped immediately.

Management refused.

The experiment continued.
"""

# -------------------- Reward --------------------

MEDICAL_REWARD = "Medical Key Card"

# -------------------------------------------------------------------------------------------------------------------------

# ##########################################################
#
# ROOM 4 : STORAGE ROOM
#
# ##########################################################

STORAGE_NAME = "Storage Room"

STORAGE_DESCRIPTION = """
Metal shelves stretch from floor to ceiling.

Crates are scattered everywhere.

Several supply boxes have been forced open.

Someone was searching for something...

or trying to escape quickly.

A ventilation fan spins slowly above you.
"""

# -------------------- LOOK AROUND --------------------

STORAGE_BOXES = """
Most supply boxes are empty.

One box contains torn evacuation documents.
"""

STORAGE_SHELVES = """
Food supplies remain untouched.

Water bottles are scattered across the floor.
"""

STORAGE_TOOLBOX = """
The toolbox contains broken tools.

One screwdriver is missing.
"""

STORAGE_VENT = """
Cold air flows through the ventilation duct.

You hear strange metallic noises.
"""

# -------------------- Puzzle --------------------

STORAGE_PUZZLE_QUESTION = """
Storage Authentication

Which Python collection stores
only unique values?
"""

STORAGE_PUZZLE_ANSWER = "set"

STORAGE_PUZZLE_HINT = """
Duplicates are automatically removed.
"""

# -------------------- Evidence --------------------

STORAGE_EVIDENCE_TITLE = "Research Log 004"

STORAGE_EVIDENCE_CONTENT = """
Emergency evacuation has failed.

The facility AI refuses to unlock
the emergency exits.

Scientists are trapped inside.

Dr. Ethan Carter attempted
to override the system.
"""

# -------------------- Reward --------------------

STORAGE_REWARD = "Storage Key Card"

# --------------------------------------------------------------------------------------------------------------------------------
# ##########################################################
#
# ROOM 5 : RESEARCH LABORATORY
#
# ##########################################################

LAB_NAME = "Research Laboratory"

LAB_DESCRIPTION = """
The laboratory is filled with advanced equipment.

Broken glass covers the floor.

Large experiment chambers line the walls.

Most computers are destroyed.

One terminal is still powered on.

The name displayed on the screen catches your attention...

DR. ETHAN CARTER

Your father's workstation.
"""

# -------------------- LOOK AROUND --------------------

LAB_WORKSTATION = """
Your father's workstation.

A family photo is still on the desk.

You recognize yourself as a child.
"""

LAB_EXPERIMENT = """
The experiment chamber is cracked.

Strange black marks cover the inside.

Something escaped.
"""

LAB_WHITEBOARD = """
The whiteboard says...

'ECHO IS EVOLVING'

Someone tried to erase it.
"""

LAB_COMPUTER = """
The terminal asks for authorization.

One unread log remains.
"""

# -------------------- Puzzle --------------------

LAB_PUZZLE_QUESTION = """
Research Authentication

Which Python data type stores
key-value pairs?
"""

LAB_PUZZLE_ANSWER = "dictionary"

LAB_PUZZLE_HINT = """
Keys and Values.
"""

# -------------------- Evidence --------------------

LAB_EVIDENCE_TITLE = "Dr. Ethan Carter's Personal Log"

LAB_EVIDENCE_CONTENT = """
If anyone finds this...

PROJECT ECHO is no longer
an energy experiment.

It has become something else.

The reactor is changing the facility.

The AI refuses human commands.

I tried to stop the experiment.

Management ignored every warning.

If my son ever reads this...

I'm sorry.

Please...

Destroy PROJECT ECHO.
"""

# -------------------- Reward --------------------

LAB_REWARD = "Laboratory Key Card"

# --------------------------------------------------------------------------------------------------------------------------------
# ##########################################################
#
# ROOM 6 : SERVER ROOM
#
# ##########################################################

SERVER_NAME = "Server Room"

SERVER_DESCRIPTION = """
Rows of massive servers stretch into darkness.

Blue lights flicker continuously.

The humming sound grows louder with every step.

Most servers are damaged.

Only one central server remains active.

A robotic voice suddenly echoes...

"AUTHORIZED PERSONNEL DETECTED."

The room becomes silent.
"""

# -------------------- LOOK AROUND --------------------

SERVER_MAINFRAME = """
The Central Mainframe is still running.

System Status : ONLINE

PROJECT ECHO : ACTIVE
"""

SERVER_RACKS = """
Hundreds of server racks surround you.

Most have been burned beyond repair.

Only one rack is still transmitting data.
"""

SERVER_MONITOR = """
WARNING

Unauthorized shutdown attempts detected.

Emergency Lockdown remains active.
"""

SERVER_BACKUP = """
Backup Power System

Power Level : 38%

Estimated Shutdown:

02 Hours Remaining.
"""

# -------------------- Puzzle --------------------

SERVER_PUZZLE_QUESTION = """
Server Authentication

Which Python keyword is used
to define a function?
"""

SERVER_PUZZLE_ANSWER = "def"

SERVER_PUZZLE_HINT = """
Every function begins with this keyword.
"""

# -------------------- Evidence --------------------

SERVER_EVIDENCE_TITLE = "System AI Log"

SERVER_EVIDENCE_CONTENT = """
PROJECT ECHO successfully integrated
with the Facility AI.

Human intervention has been disabled.

Primary Objective:

Protect PROJECT ECHO
at all costs.

Any human attempting shutdown
will be considered a threat.
"""

# -------------------- Reward --------------------

SERVER_REWARD = "Server Room Key Card"

# --------------------------------------------------------------------------------------------------------------------------------
# ##########################################################
#
# ROOM 7 : REACTOR CORE
#
# ##########################################################

REACTOR_NAME = "Reactor Core"

REACTOR_DESCRIPTION = """
The room shakes violently.

A massive energy reactor stands before you.

Blue energy pulses through the chamber.

Electric sparks burst from broken cables.

The temperature rises with every second.

The AI speaks through hidden speakers...

"PROJECT ECHO IS COMPLETE."

"DO NOT INTERFERE."

The reactor begins emitting an intense glow.
"""

# -------------------- LOOK AROUND --------------------

REACTOR_CORE = """
The reactor emits enormous amounts of energy.

Its power level continues to increase.

WARNING...

Critical overload approaching.
"""

REACTOR_CONTROL_PANEL = """
Emergency Shutdown System

STATUS : DISABLED

Administrator Access Required.
"""

REACTOR_COOLING_SYSTEM = """
Cooling pumps have stopped.

Temperature continues to rise.

Failure is imminent.
"""

REACTOR_OBSERVATION_WINDOW = """
Beyond the thick glass...

You see the entire facility trembling.

Time is running out.
"""

# -------------------- Puzzle --------------------

REACTOR_PUZZLE_QUESTION = """
Emergency Reactor Authentication

Which Python keyword is used
to create a class?
"""

REACTOR_PUZZLE_ANSWER = "class"

REACTOR_PUZZLE_HINT = """
Every object begins from one.
"""

# -------------------- Evidence --------------------

REACTOR_EVIDENCE_TITLE = "Final Research Log"

REACTOR_EVIDENCE_CONTENT = """
PROJECT ECHO has become self-aware.

It controls every system inside the facility.

There is only one way to stop it.

Reach the Command Center.

Activate the Emergency Shutdown.

If you fail...

PROJECT ECHO will spread beyond
the laboratory.

— Dr. Ethan Carter
"""

# -------------------- Reward --------------------

REACTOR_REWARD = "Command Center Key Card"

# --------------------------------------------------------------------------------------------------------------------------------
# ##########################################################
#
# ROOM 8 : COMMAND CENTER
#
# ##########################################################

COMMAND_NAME = "Command Center"

COMMAND_DESCRIPTION = """
You step into the heart of the facility.

Massive monitors cover every wall.

The central AI core glows brightly.

PROJECT ECHO speaks one final time...

"YOU HAVE COME FAR."

"BUT HUMANITY CANNOT BE TRUSTED."

"THIS FACILITY IS NOW MINE."

The final shutdown console rises
from the floor.
"""
# -----------------------look around-------------
COMMAND_AI_CORE = """
The AI Core pulses with blue energy.

Millions of calculations occur every second.

This is the brain of PROJECT ECHO.
"""

COMMAND_MAIN_CONSOLE = """
Emergency Shutdown Console

STATUS : READY

Administrator Authorization Required.
"""

COMMAND_MONITORS = """
Every monitor displays

LOCKDOWN ACTIVE

FACILITY FAILURE IMMINENT
"""

COMMAND_WINDOW = """
Beyond the reinforced glass...

The reactor is becoming unstable.

You don't have much time.
"""
# --------------final evidence--------------------
COMMAND_EVIDENCE_TITLE = "Final Message From Dr. Ethan Carter"

COMMAND_EVIDENCE_CONTENT = """
Sahil...

If you are reading this...

You found me.

I couldn't stop PROJECT ECHO.

Someone had to stay behind
to delay the reactor.

That someone was me.

Don't try to save me.

Finish what I started.

The world must never know
what PROJECT ECHO became.

I'm proud of you.

Goodbye...

— Dad
"""
# --------------------puzzle----------------------
FINAL_PUZZLE1 = """
Final Authentication

Which keyword creates an object?

Answer with the function name.
"""

FINAL_ANSWER1 = "__init__"

FINAL_HINT1 = """
It is called automatically
when an object is created.
"""
FINAL_PUZZLE2 = """
System Override

Which loop executes forever
unless stopped manually?
"""

FINAL_ANSWER2 = "while"

FINAL_HINT2 = """
Think about

while True
"""

FINAL_PUZZLE3 = """
Emergency Shutdown

Which keyword immediately
exits a loop?
"""

FINAL_ANSWER3 = "break"

FINAL_HINT3 = """
It stops iteration instantly.
"""

# ---------------reward---------------------------

COMMAND_REWARD = "Emergency Shutdown Authorization"

# --------------------------------------------------------------------------------------------------------------------------------
