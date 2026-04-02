from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")
    if operation in ("add", "multiply"):
        return reduce(ops[operation], spells)
    else:
        return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment,
                                power=50,
                                element="fire"),
        "ice_enchant": partial(base_enchantment,
                               power=50,
                               element="ice"),
        "lightning_enchant": partial(base_enchantment,
                                     power=50,
                                     element="lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(arg):
        return f"Unknown spell type: {type(arg)}"

    @cast.register
    def _(arg: int):
        return f"Damage spell deals {arg} damage!"

    @cast.register
    def _(arg: str):
        return f"Enchantment applied: {arg}"

    @cast.register
    def _(arg: list):
        results = [cast(a) for a in arg]
        return results

    return cast


if __name__ == "__main__":
    try:
        print("\nTesting spell_reducer...")
        spells = [10, 20, 30, 40]
        print("Sum:", spell_reducer(spells, "add"))
        print("Product:", spell_reducer(spells, "multiply"))
        print("Max:", spell_reducer(spells, "max"))
    except Exception as e:
        print(e)
    try:
        print("\nTesting memoized_fibonacci...")
        print("Fib(10):", memoized_fibonacci(10))
        print("Fib(15):", memoized_fibonacci(15))
    except Exception as e:
        print(e)
