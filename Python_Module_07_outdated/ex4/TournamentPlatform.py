from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        print("Creating tournament match...")
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        result = card1.attack(card2)
        winner = result["winner"]
        loser = result["loser"]
        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self.cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        total = len(self.cards)
        avg_rating = sum(c.rating for c in self.cards.values()) // total
        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
