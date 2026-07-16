============================================================
                       PROJECT ECHO
             Terminal-Based Escape Room Adventure
                       Version 1.0
============================================================

DEVELOPED BY
------------
Sahil Rai

Special Thanks: Ajay Thakur Sir (Trainer), ChatGPT (Planning & Mentoring)


ABOUT
-----
You play a scientist's child who has broken into the abandoned
Helix Research Facility to learn the truth about PROJECT ECHO,
the experiment that took your father from you. Explore eight
rooms, solve Python-themed authentication puzzles, collect key
cards and evidence, and reach the Command Center before the
facility -- and PROJECT ECHO itself -- stop you.


HOW TO RUN
----------
    python main.py

Requires Python 3.10+ (the project uses match-case statements).


HOW TO PLAY
-----------
- Explore each room with "Look Around" to find story clues.
- Solve the room's puzzle to unlock its reward and access level.
- Wrong puzzle answers cost you health -- run out and it's game over.
- Collect the reward to raise your access level and move forward.
- Read Evidence Files to piece together what really happened.
- Reach the Command Center and complete the Final Shutdown
  Sequence to end the game.


PROJECT STRUCTURE
------------------
    main.py             Entry point
    game.py              Game class: menus, room flow, ending
    menu.py              Main menu screens
    player.py            Player stats, HUD, backpack access
    backpack.py          Inventory container (holds Item objects)
    item.py              A single collectible item
    room.py               Room behaviour (look, solve, collect, evidence)
    puzzle.py             Puzzle question/answer/hint logic
    evidence.py           A single evidence file
    final_challenge.py    The three-part Command Center puzzle
    utils.py              Shared print/input helper functions
    data.py                All story text, room text, and puzzle data
