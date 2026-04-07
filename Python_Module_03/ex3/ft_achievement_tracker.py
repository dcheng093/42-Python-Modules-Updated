#!/usr/bin/python3.10

import random

ACHIEVEMENTS = [
    "First Steps", "Speed Runner", "Survivor", "Strategist",
    "Master Explorer", "Treasure Hunter", "Collector Supreme",
    "Untouchable", "Boss Slayer", "Sharp Mind",
    "Crafting Genius", "World Savior", "Unstoppable",
    "Hidden Path Finder"
]


def gen_player_achievements():
    count = random.randint(3, 8)
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    for name, ach in players.items():
        print(f"Player {name}: {ach}")
    all_achievements: set = set()
    for ach in players.values():
        all_achievements = all_achievements.union(ach)
    print(f"\nAll distinct achievements: {all_achievements}\n")
    common = None
    for ach in players.values():
        if common is None:
            common = ach
        else:
            common = common.intersection(ach)
    print(f"Common achievements: {common}\n")
    for name, ach in players.items():
        others: set = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = others.union(other_ach)
        unique = ach.difference(others)
        print(f"Only {name} has: {unique}")
    print()
    for name, ach in players.items():
        missing = set(ACHIEVEMENTS).difference(ach)
        print(f"{name} is missing: {missing}")

# def achievement_tracker(players):
#     print("=== Achievement Tracker System ===\n")
#     for player in players:
#         print(f"Player {player} achievements: {players[player]}")
#     print("=== Achievement Analysis ===\n")
#     unique_achievements = set()
#     for player in players:
#         unique_achievements = unique_achievements.union(players[player])
#     print(f"All unique achievements: {unique_achievements}")
#     print(f"Total unique achievements: {len(unique_achievements)}\n")
#     common = None
#     for player in players:
#         if common is None:
#             common = players[player]
#         else:
#             common = common.intersection(players[player])
#     print(f"Common to all players: {common}")
#     rare = set()
#     for achievements in unique_achievements:
#         count = 0
#         for player in players:
#             if achievements in players[player]:
#                 count += 1
#         if count == 1:
#             rare = rare.union({achievements})
#     print(f"Rare achievements (1 player): {rare}\n")
#     alice = players["alice"]
#     bob = players["bob"]
#     print(f"Alice vs Bob common: {alice.intersection(bob)}")
#     print(f"Alice unique: {alice.difference(bob)}")
#     print(f"Bob unique: {bob.difference(alice)}")


# if __name__ == "__main__":
#     players = {"alice": {'speed_demon', 'level_10', 'treasure_hunter',
#                          'first_kill'},

#                "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},

#                "charlie": {'level_10', 'treasure_hunter', 'boss_slayer',
#                            'speed_demon',
#                            'perfectionist'}}
#     achievement_tracker(players)
