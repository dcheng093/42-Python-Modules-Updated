from alchemy import create_air


def main():
    return (create_air())


if __name__ == "__main__":
    print("=== Alembic 5 ===\n"
          "Accessing the alchemy module using 'from alchemy import ...'\n"
          f"Tesing create_air: {main()}\n")
