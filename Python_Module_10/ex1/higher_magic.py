def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs),
                spell2(*args, **kwargs)
                )
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


if __name__ == "__main__":
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def lightning(target):
        return f"Lightning strikes {target}"

    def is_alive(target):
        return target != "ghost"
    print("\nTesting spell_combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon")
    print(f"Combined spell result: {result1}, {result2}")
    print("\nTesting power_amplifier...")

    def simple_fireball():
        return 10
    mega_fireball = power_amplifier(simple_fireball, 3)
    print(f"Original: {simple_fireball()}, Amplified: {mega_fireball()}")
