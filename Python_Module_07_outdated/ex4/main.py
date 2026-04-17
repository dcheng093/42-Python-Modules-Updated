from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard


def print_card_info(card: TournamentCard) -> None:
    print(f"{card.name} (ID: {card.card_id}):\n"
          "- Interfaces: [Card, Combatable, Rankable]\n"
          f"- Rating: {card.rating}\n"
          f"- Record: {card.wins}-{card.losses}\n")


def main():
    print("\n=== DataDeck Tournament Platform ===\n"
          "\nRegistering Tournament Cards...\n")
    platform = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon",
                            5,
                            "Legendary",
                            0,
                            0,
                            1200,
                            "dragon_001")
    wizard = TournamentCard("Ice Wizard",
                            4,
                            "Epic",
                            0,
                            0,
                            1150,
                            "wizard_001")

    platform.register_card(dragon)
    print_card_info(dragon)
    platform.register_card(wizard)
    print_card_info(wizard)
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result, "\n"
          "Tournament Leaderboard:")
    for i, card in enumerate(platform.get_leaderboard(), start=1):
        print(f"{i}. {card.name} - "
              f"Rating: {card.rating} ({card.wins}-{card.losses})")
    print("\nPlatform Report:",
          platform.generate_tournament_report(),
          "\n\n=== Tournament Platform Successfully Deployed! ===\n"
          "All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
