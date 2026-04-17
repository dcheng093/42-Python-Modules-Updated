from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack_power: int,
                 defense_power: int,
                 mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            "card": self.name,
            "status": "played",
            "type": "elite"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense_power, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power,
                "defense": self.defense_power}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = min(4, self.mana)
        self.mana -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        channeled = amount - self.mana
        self.mana = amount
        return {
            "channeled": channeled,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
