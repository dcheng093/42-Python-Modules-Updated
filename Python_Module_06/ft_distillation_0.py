from alchemy.potions import healing_potion, strength_potion


def main():
    print("=== Distillation 0 ===\n"
          "Direct access to alchemy/potions.py\n"
          f"Testing strength potion: {strength_potion()}\n"
          f"Testing healing potion: {healing_potion()}\n")


if __name__ == "__main__":
    main()
