import random
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards += [card]

    def remove_card(self, card_name: str) -> bool:
        for car in self.cards:
            if car.name == card_name:
                self.cards.remove(car)
                return True
            return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        total_cards = 0
        spell_count = 0
        artifact_count = 0
        cost_total = 0
        for i, card in enumerate(self.cards):
            total_cards += 1
            cost_total += card.cost
            if card.__class__.__name__ == "SpellCard":
                spell_count += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifact_count += 1

        avg_cost = 0.0
        if total_cards > 0:
            avg_cost = float((cost_total + total_cards - 1) // total_cards)
        return {
            "total_cards": total_cards,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": avg_cost
        }
