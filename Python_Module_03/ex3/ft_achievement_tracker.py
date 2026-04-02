#!/usr/bin/python3.10

def achievement_tracker(players):
    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(f"Player {player} achievements: {players[player]}")
    print("=== Achievement Analysis ===\n")
    unique_achievements = set()
    for player in players:
        unique_achievements = unique_achievements.union(players[player])
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")
    common = None
    for player in players:
        if common is None:
            common = players[player]
        else:
            common = common.intersection(players[player])
    print(f"Common to all players: {common}")
    rare = set()
    for achievements in unique_achievements:
        count = 0
        for player in players:
            if achievements in players[player]:
                count += 1
        if count == 1:
            rare = rare.union({achievements})
    print(f"Rare achievements (1 player): {rare}\n")
    alice = players["alice"]
    bob = players["bob"]
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    players = {"alice": {'speed_demon', 'level_10', 'treasure_hunter',
                         'first_kill'},

               "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},

               "charlie": {'level_10', 'treasure_hunter', 'boss_slayer',
                           'speed_demon',
                           'perfectionist'}}
    achievement_tracker(players)
