from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===\n"
          "\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}\n"
          f"Strategy: {strategy.get_strategy_name()}\n"
          f"Available types: {factory.get_supported_types()}\n"
          f"\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()
    print(f"Hand: {engine.hand}\n"
          "\nTurn execution:"
          f"\nStrategy: {strategy.get_strategy_name()}\n"
          f"Actions: {turn_result}")
    game_report = engine.get_engine_status()
    print("\nGame Report:\n"
          f"{game_report}\n"
          "\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
