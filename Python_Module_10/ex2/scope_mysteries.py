def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(power: int) -> int:
        nonlocal total
        total += power
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value):
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":

    print("\nTesting mage_counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())
    print("\nTesting enchantment_factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
