import alchemy.elements


def main():
    return (alchemy.elements.create_earth())


if __name__ == "__main__":
    print("=== Alembic 2 ===\n"
          "Accessing alchemy/elements.py using 'import ...' structure\n"
          f"Testing create_earth: {main()}\n")
