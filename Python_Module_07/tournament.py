from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def format_opponents(opponents):
    result = []

    for factory, strategy in opponents:
        factory_name = factory.__class__.__name__
        if factory_name in ["FlameFactory", "AquaFactory"]:
            creature_name = factory.create_base().name
        elif factory_name == "HealingCreatureFactory":
            creature_name = "Healing"
        elif factory_name == "TransformCreatureFactory":
            creature_name = "Transform"
        else:
            creature_name = factory_name.replace("Factory", "")
        strategy_name = strategy.__class__.__name__.replace("Strategy", "")
        result.append(f"({creature_name}+{strategy_name})")
    return " [ " + ", ".join(result) + " ]"


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]
            c1 = factory1.create_base()
            c2 = factory2.create_base()
            print("\n* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            try:
                for action in strat1.act(c1):
                    print(action)
                for action in strat2.act(c2):
                    print(action)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main():
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    print("Tournament 0 (basic)")
    print(format_opponents([
        (flame, normal),
        (healing, defensive)
    ]))
    battle([
        (flame, normal),
        (healing, defensive)
    ])
    print("\nTournament 1 (error)")
    print(format_opponents([
        (flame, aggressive),
        (healing, defensive)
    ]))
    battle([
        (flame, aggressive),
        (healing, defensive)
    ])
    print("\nTournament 2 (multiple)")
    print(format_opponents([
        (aqua, normal),
        (healing, defensive),
        (transform, aggressive)
    ]))
    battle([
        (aqua, normal),
        (healing, defensive),
        (transform, aggressive)
    ])


if __name__ == "__main__":
    main()
