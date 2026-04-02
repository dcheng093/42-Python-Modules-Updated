import time
from functools import wraps


def spell_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start + 0.001:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[1] >= min_power:
                return func(*args, **kwargs)
            else:
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
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    try:
        print("\nTesting spell_timer...")

        @spell_timer
        def fireball():
            time.sleep(0.1)
            return "Fireball cast!"
        result = fireball()
        print("Result:", result)
    except Exception as e:
        print(e)
    try:
        print("\nTesting MageGuild...")
        guild = MageGuild()
        print(MageGuild.validate_mage_name("Gandalf"))
        print(MageGuild.validate_mage_name("Al"))
        print(guild.cast_spell(15, "Lightning"))
        print(guild.cast_spell(5, "Lightning"))
    except Exception as e:
        print(e)
