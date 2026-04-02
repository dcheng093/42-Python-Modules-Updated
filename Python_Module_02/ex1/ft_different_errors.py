def garden_operations():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        missing = {"flowers": 5}
        print(missing["plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        print("Testing multiple errors together...")
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()


if __name__ == "__main__":
    test_error_types()
