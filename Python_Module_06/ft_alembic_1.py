from elements import create_water


def main():
    return (create_water())


if __name__ == "__main__":
    print("=== Alembic 1 ==="
          "\nUsing 'from ... import ...' structure to access elements.py"
          f"\nTesting create_water: {main()}\n")
