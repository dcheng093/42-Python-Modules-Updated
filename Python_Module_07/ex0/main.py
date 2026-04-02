from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n"
          "\nTesting Abstract Base Class Design:\n")
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )
    print("CreatureCard Info:\n" +
          str(fire_dragon.get_card_info()),
          "\n\nPlaying Fire Dragon with 6 mana available:",
          "\nPlayable:", fire_dragon.is_playable(6),
          "\nPlay result:", fire_dragon.play({}),
          "\n\nFire Dragon attacks Goblin Warrior:\n" +
          "Attack result:" +
          str(fire_dragon.attack_target("Goblin Warrior")),
          "\n\nTesting insufficient mana (3 available):",
          "\nPlayable:", fire_dragon.is_playable(3),
          "\n\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
