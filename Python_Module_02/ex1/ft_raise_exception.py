#!/usr/bin/python3.10

def input_temperature(temp_str):
    try:
        num = int(temp_str)
        if num < 0:
            print(f"Caugt input_temperature error: {num}°C is too cold for plants (min 0°C)\n")
        elif num > 40:
            print(f"Caugt input_temperature error: {num}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature is now {num}°C\n")
        return num
    except ValueError as e:
        print(f"Caugt input_temperature error: {e}\n")


def test_temperature():
    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"Testing temperature: {test}")
        check_temperature(test)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()