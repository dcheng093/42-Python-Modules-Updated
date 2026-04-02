#!/usr/bin/python3.10
import sys


def parse_inventory(args):
    """Parse command-line args like sword:1 potion:5 into a dict"""
    inventory = {}
    for arg in args:
        if ":" in arg:
            name, qty = arg.split(":")
            inventory[name] = int(qty)
    return inventory


def display_inventory_stats(inventory):
    total_items = sum(inventory.values())
    unique_items = len(inventory)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print("\n=== Current Inventory ===")
    for item, qty in sorted(inventory.items(), key=lambda x: -x[1]):
        percent = (qty / total_items) * 100
        print(f"{item}: {qty} unit{'s' if qty > 1 else ''} ({percent:.1f}%)")
    most_item = max(inventory.items(), key=lambda x: x[1])
    least_item = min(inventory.items(), key=lambda x: x[1])
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_item[0]} ({most_item[1]} units)")
    print(f"Least abundant: {least_item[0]} ({least_item[1]} units)")
    moderate = {k: v for k, v in inventory.items() if v > 3}
    scarce = {k: v for k, v in inventory.items() if v <= 3}
    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    restock = [item for item, qty in inventory.items() if qty == 1]
    print("\n=== Management Suggestions ===")
    if restock:
        print("Restock needed:", ", ".join(restock))
    else:
        print("All items sufficiently stocked")
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in inventory.values()))
    sample_item = 'sword'
    print(f"Sample lookup - '{sample_item}' in inventory:",
          sample_item in inventory)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py sword:1 potion:5 ...")
        sys.exit(1)
    inventory = parse_inventory(sys.argv[1:])
    display_inventory_stats(inventory)
