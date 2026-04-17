from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple:
        return (
            spell1(*args, **kwargs),
            spell2(*args, **kwargs),
        )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon", 10)
    print(f"Combined spell result: {result1}, {result2}")
    print("\nTesting power amplifier...")

    def simple_fireball(target: str, power: int) -> int:
        return power

    mega_fireball = power_amplifier(simple_fireball, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")
