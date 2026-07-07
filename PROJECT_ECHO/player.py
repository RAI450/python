from backpack import Backpack


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.access_level = 0
        self.backpack = Backpack()
        self.evidence_list = []

    # =====================================================

    def show_player_info(self):

        print(f"""
---------------- PLAYER PROFILE ----------------

            Name         : {self.name}
            Health       : {self.health}
            Score        : {self.score}
            Access Level : {self.access_level}
------------------------------------------------

""")

    # =====================================================

    def show_backpack(self):
        

        print("""
    ---------------- BACKPACK ----------------
    """)

        if self.backpack.items:

            for i, item in enumerate(self.backpack.items, 1):

                print(f"{i}. {item}")

        else:

            print("Backpack is empty.")

        print("""
    
    """)

    # =====================================================

    def show_evidence(self):

        print("""
    ---------------- EVIDENCE FILES ----------------
    """)

        if self.evidence_list:

            for i, evidence in enumerate(self.evidence_list, 1):

                print(f"{i}. {evidence}")

        else:

            print("No evidence collected.")

        print("""
    
    """)

    # =====================================================

    def take_damage(self, damage):

        self.health -= damage

        if self.health < 0:
            self.health = 0

    # =====================================================

    def heal(self, amount):

        self.health += amount

        if self.health > 100:
            self.health = 100

    # =====================================================

    def add_score(self, points):

        self.score += points

    # =====================================================

    def increase_access_level(self):

        self.access_level += 1

    # =====================================================

    def add_evidence(self, evidence):

        self.evidence_list.append(evidence)

    # =====================================================

    def add_item(self, item):

        self.backpack.add_item(item)

    def show_hud(self):

        print(f"""
    ========================================================
                       Player Status
    ========================================================
            Player       : {self.name.title()}
            Health       : {self.health}
            Score        : {self.score}
            Access Level : {self.access_level}
            Evidence     : {len(self.evidence_list)}
            Items        : {len(self.backpack.items)}
    
    --------------------------------------------------------
    """)