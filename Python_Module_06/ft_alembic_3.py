from alchemy.elements import create_air


def main():
    return (create_air())


if __name__ == "__main__":
    print("=== Alembic 3 ===\n"
          "Accessing alchemy/elements.py using 'from ... import ...' structure"
          f"\nTesting create_air: {main()}\n")
