from alchemy.transmutation import recipes


def main():
    print("=== Transmutation 0 ===\n"
          "Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {recipes.lead_to_gold()}\n")


if __name__ == "__main__":
    main()
