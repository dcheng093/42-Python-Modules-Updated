def ft_seed_inventory(seed: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed.capitalize(), "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(seed.capitalize(), "seeds:", quantity, unit, "total")
    elif unit == "area":
        print(seed.capitalize(), "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
