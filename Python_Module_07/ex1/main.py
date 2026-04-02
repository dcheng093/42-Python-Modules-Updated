from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.Card import Card


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare",
                               durability=5, effect="+1 mana per turn"))

    class CreatureCard(Card):
        def play(self, game_state):
            return {"card_played": self.name, "mana_used": self.cost, "effect":
                    "Creature summoned to battlefield"}

    deck.add_card(CreatureCard("Fire Dragon", 5, "Epic"))
    print("Building deck with different card types...\n"
          "Deck stats:",
          deck.get_deck_stats(),
          "\n\nDrawing and playing cards:\n")
    game_state = {}
    deck.shuffle()
    while deck.cards:
        card = deck.draw_card()
        result = card.play(game_state)
        print(f"Drew: {card.name} ({card.card_type})")
        print("Play result:", result, "\n")
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
