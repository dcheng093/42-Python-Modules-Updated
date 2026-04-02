from ex0.Card import Card


class SpellCard(Card):
    card_type = "Spell"

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        result = self.resolve_effect(targets=[])
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": result
        }

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == "damage":
            return f"Deal {self.cost} damage to target"
        elif self.effect_type == "heal":
            return f"Heal {self.cost} HP"
        else:
            return f"Apply {self.effect_type}"
