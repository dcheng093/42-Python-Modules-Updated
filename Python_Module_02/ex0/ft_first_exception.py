# !/usr/bin/python3.10

def input_temperature(temp_str: str) -> int:
    try:
        num = int(temp_str)
        if num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)\n")
        elif num > 40:
            print(f"Error: {num}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature is now {num}°C\n")
        return num
    except ValueError as e:
        print(f"Caugt input_temperature error: {e}\n")


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    tests = ["25", "abc"]

    for test in tests:
        print(f"Input data is '{test}'")
        input_temperature(test)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
