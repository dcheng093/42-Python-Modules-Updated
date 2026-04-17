import time
from functools import wraps


def spell_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power):
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


def retry_spell(max_attempts):
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
                        return ("Spell casting failed after max_attempts "
                                "attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell_timer...")

    @spell_timer
    def fireball():
        time.sleep(0.098)
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
