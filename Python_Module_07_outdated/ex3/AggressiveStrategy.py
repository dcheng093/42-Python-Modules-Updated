from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        actions = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 0
        }
        mana = 5
        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= mana:
                actions["cards_played"].append(card.name)
                actions["mana_used"] += card.cost
                mana -= card.cost

                if hasattr(card, "attack"):
                    actions["damage_dealt"] += card.attack
                else:
                    actions["damage_dealt"] += card.cost
        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
