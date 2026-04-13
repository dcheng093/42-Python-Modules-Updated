import alchemy


def main():
    print("=== Distillation 1 ===\n"
          "Direct access to alchemy/potions.py\n"
          f"Testing strength potion: {alchemy.strength_potion()}\n"
          f"Testing heal alias: {alchemy.heal()}\n")


if __name__ == "__main__":
    main()
