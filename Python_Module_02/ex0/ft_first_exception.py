#!/usr/bin/python3.10

def check_temperature(temp_str):
    try:
        num = int(temp_str)
        if num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)\n")
        elif num > 40:
            print(f"Error: {num}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {num}°C is perfect for plants!\n")
        return num
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"Testing temperature: {test}")
        check_temperature(test)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
