from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")
    elite = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        attack_power=5,
        defense_power=3,
        mana=4
    )
    print("EliteCard capabilities:\n",
          "- Card: ['play', 'get_card_info', 'is_playable']\n",
          "- Combatable: ['attack', 'defend', 'get_combat_stats']\n",
          "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n",
          "\nPlaying Arcane Warrior (Elite Card):\n"
          "\nCombat phase:")
    attack_result = elite.attack("Enemy")
    print(f"Attack result: {attack_result}")
    defense_result = elite.defend(5)
    print(f"Defense result: {defense_result}",
          "\n\nMagic phase:")
    mana_result = elite.channel_mana(7)
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")
    print(f"Mana channel: {mana_result}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
