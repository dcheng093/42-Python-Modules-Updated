from abc import ABC, abstractmethod
from ex1.Capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> list:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> list:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature) -> list:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )

        return [
            creature.transform(),
            creature.attack(),
            creature.revert()
        ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature) -> list:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive "
                "strategy"
            )

        return [
            creature.attack(),
            creature.heal()
        ]