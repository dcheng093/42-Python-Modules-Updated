class GameEngine:
    def configure_engine(self, factory, strategy):
        deck = factory.create_themed_deck(3)
        self.factory = factory
        self.strategy = strategy
        self.hand = deck["creatures"] + deck["spells"]
        self.battlefield = []
        self.turns = 0
        self.total_damage = 0

    def simulate_turn(self) -> dict:
        self.turns += 1
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.total_damage += turn_result["damage_dealt"]
        return turn_result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }
