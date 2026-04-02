from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


class ArtifactCard(Card):
    def play(self, game_state: dict) -> dict:
        return game_state


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power=None):
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon",
                                5,
                                "Rare",
                                attack=5,
                                health=8)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior",
                                2,
                                "Common",
                                attack=5,
                                health=2)

    def create_spell(self, name_or_power=None) -> Card:
        if name_or_power == "fireball":
            return SpellCard("Fireball",
                             3,
                             "Common",
                             effect_type="damage")
        elif name_or_power == "lightning":
            return SpellCard("Lightning Bolt",
                             3,
                             "Common",
                             effect_type="damage")

    def create_artifact(self, name_or_power=None) -> Card:
        return ArtifactCard("Mana Ring",
                            1,
                            "Uncommon")

    def create_themed_deck(self, size: int) -> dict:
        return {
            "creatures": [self.create_creature("dragon"),
                          self.create_creature("goblin")],
            "spells": [self.create_spell("lightning")],
            "artifacts": [self.create_artifact("mana_ring")]
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
