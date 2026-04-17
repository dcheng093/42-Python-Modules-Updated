from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 wins: int,
                 losses: int,
                 rating: int,
                 card_id: str) -> None:
        super().__init__(name, cost, rarity)
        self.wins = 0
        self.losses = 0
        self.rating = rating
        self.card_id = card_id

    def attack(self, target) -> dict:
        if self.rating >= target.rating:
            return {"winner": self, "loser": target}
        return {"winner": target, "loser": self}

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

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
