#!/usr/bin/python3.10

def display_inventory(player_name, player_dict):
    print(f"=== {player_name}'s Inventory ===\n")
    inventory = player_dict.get(player_name, {})
    total_val = 0
    total_items = 0
    cat = {}
    for item, details in inventory.items():
        item_type = details.get("type")
        rarity = details.get("rarity")
        qty = details.get("quantity")
        val = details.get("value")
        print(f"{item} ({item_type}, {rarity}): {qty}x @ {val} gold each = "
              f"{qty * val} gold")
        total_val += qty * val
        total_items += qty
        cat[item_type] = cat.get(item_type, 0) + qty
    print("")
    print(f"Inventory value: {total_val} gold")
    print(f"Item count: {total_items} items")
    print("Categories: ", end="")
    cat_items = cat.items()
    count = 0
    total_cats = len(cat)
    for name, qty in cat_items:
        count += 1
        print(f"{name}({qty})", end="")
        if count < total_cats:
            print(", ", end="")
    print("")


def transaction_update(player1, player2, item_name, qty, player_dict):
    inv1 = player_dict.get(player1)
    inv2 = player_dict.get(player2)
    item_data = inv1.get(item_name)
    if item_data and item_data.get("quantity") >= qty:
        item_data["quantity"] -= qty
        if item_name not in inv2:
            inv2[item_name] = {
                "type": item_data.get("type"),
                "rarity": item_data.get("rarity"),
                "quantity": qty,
                "value": item_data.get("value")
            }
        else:
            inv2[item_name]["quantity"] += qty
        print("")
        print(f"=== Transaction: {player1} gives {player2} {qty} {item_name}s"
              " ===")
        print("Transaction successful!")
        print("")
        p1_qty = inv1.get(item_name).get("quantity")
        p2_qty = inv2.get(item_name).get("quantity")
        print("=== Updated Inventories ===")
        print(f"{player1} {item_name}: {p1_qty}")
        print(f"{player2} {item_name}: {p2_qty}")
        print("")
    else:
        print("Transaction failed: Not enough items!")
        print("")


def display_analytics(player_dict):
    print("=== Inventory Analytics ===")
    mvp_name = ""
    max_gold = 0
    most_items_name = ""
    max_items = 0
    for name, inv in player_dict.items():
        current_total = 0
        item_count = 0
        for details in inv.values():
            current_total += details.get("quantity") * details.get("value")
            item_count += details.get("quantity")
        if current_total > max_gold:
            max_gold = current_total
            mvp_name = name
        if item_count > max_items:
            max_items = item_count
            most_items_name = name
    print(f"Most valuable player: {mvp_name} ({max_gold} gold)")
    print(f"Most items: {most_items_name} ({max_items} items)")
    rare_items = {}
    for inv in player_dict.values():
        for item, details in inv.items():
            if details.get("rarity") == "rare":
                rare_items[item] = True
    if rare_items:
        print("Rarest items: ", end="")
        count = 0
        total = len(rare_items)
        for item in rare_items.keys():
            count += 1
            print(item, end="")
            if count < total:
                print(", ", end="")
        print("")
    print("")


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    players = {
        "Alice": {
            "sword": {"type": "weapon", "rarity": "rare", "quantity": 1,
                      "value": 500},
            "potion": {"type": "consumable", "rarity": "common", "quantity": 5,
                       "value": 50},
            "shield": {"type": "armor", "rarity": "uncommon", "quantity": 1,
                       "value": 200}
        },
        "Bob": {
            "magic_ring": {"type": "ring", "rarity": "rare", "quantity": 1,
                           "value": 1}
        }
    }
    display_inventory("Alice", players)
    transaction_update("Alice", "Bob", "potion", 2, players)
    display_analytics(players)
