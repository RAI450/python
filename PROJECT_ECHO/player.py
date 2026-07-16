from backpack import Backpack
from utils import print_header, progress_bar

TOTAL_ROOMS = 8


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
        print_header("Player Profile")

        print(f"""            Name         : {self.name}
            Health       : {self.health} / 100
            Score        : {self.score}
            Access Level : {self.access_level}
""")

    # =====================================================

    def show_backpack(self):
        self.backpack.inspect_items()

    # =====================================================

    def show_evidence(self):
        print_header("Evidence Files")

        if self.evidence_list:
            for i, evidence in enumerate(self.evidence_list, 1):
                print(f"{i}. {evidence}")
        else:
            print("No evidence collected.")

        print()

    # =====================================================

    def take_damage(self, damage):
        """Reduce player health and report whether the player is
        still alive. The caller uses the return value to trigger a
        Game Over if health reaches 0."""

        self.health -= damage

        if self.health < 0:
            self.health = 0

        return self.health > 0

    # =====================================================

    def heal(self, amount):
        self.health += amount

        if self.health > 100:
            self.health = 100

    # =====================================================

    def is_alive(self):
        return self.health > 0

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
        print_header("Player Status")

        print(f"""            Player       : {self.name.title()}
            Health       : {self.health} / 100
            Score        : {self.score}
            Access Level : {self.access_level}
            Evidence     : {len(self.evidence_list)}
            Items        : {len(self.backpack.items)}

            Facility Progress : {progress_bar(self.access_level, TOTAL_ROOMS)}
""")
