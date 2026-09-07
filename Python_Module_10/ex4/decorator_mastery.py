import time
from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")

            if power is None:
                power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        print(
                            "Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
                        print("Waaaaaaagh spelled !")
                        return (f"Spell casting failed after {max_attempts} "
                                "attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and any(c.isalpha() for c in name)
            and all(c.isalpha() or c.isspace() for c in name)
            )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell_timer...")

    @spell_timer
    def fireball():
        time.sleep(0.0989)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)
    print("\nTesting retrying spell...")

    @retry_spell(3)
    def fail_spell():
        raise Exception("boom")

    fail_spell()
    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

    # print("\n\n\nexamples using the actual data from the generator:")
    # test_powers = [11, 10, 16, 9]
    # spell_names = ['lightning', 'earthquake', 'tornado', 'tsunami']
    # mage_names = ['River', 'Storm', 'Sage', 'Riley', 'Kai', 'Phoenix']
    # invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    # print("\nTesting MageGuild with generator data...")
    # guild_2 = MageGuild()

    # for spell_name, power in zip(spell_names, test_powers):
    #     print(guild.cast_spell(spell_name, power))

    # print("\nTesting mage names...")

    # for name in mage_names:
    #     print(name, MageGuild.validate_mage_name(name))

    # for name in invalid_names:
    #     print(name, MageGuild.validate_mage_name(name))
