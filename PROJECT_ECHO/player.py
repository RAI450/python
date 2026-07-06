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
================ PLAYER PROFILE ================

Name         : {self.name}
Health       : {self.health}
Score        : {self.score}
Access Level : {self.access_level}

================================================
""")

    # =====================================================

    def show_backpack(self):
        self.backpack.show_items()

    # =====================================================

    def show_evidence(self):

        if self.evidence_list:

            print("""
================ EVIDENCE =================
""")

            for evidence in self.evidence_list:
                print(f"- {evidence}")

            print("""
===========================================
""")

        else:

            print("""
No evidence collected yet.
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
    ================================================

    Player : {self.name}

    Health : {self.health}

    Score : {self.score}

    Access Level : {self.access_level}

    Backpack Items : {len(self.backpack.items)}

    Evidence Files : {len(self.evidence_list)}

    ================================================
    """)