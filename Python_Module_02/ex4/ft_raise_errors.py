#!/usr/bin/python3.10

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if len(plant_name) == 0:
        raise ValueError("Error: Plant name cannot be empty!\n")
    elif water_level < 1 or water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too "
            f"{'low (min 1)' if water_level < 1 else 'high (max 10)'}\n"
        )

    elif sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too "
            f"{'low (min 2)' if sunlight_hours < 2 else 'high (max 12)'}\n"
        )
    else:
        print(f"Plant: '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("=== Garden Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 6, 7)
    except ValueError as e:
        print(e)
    print("Testing empty plant name...")
    try:
        check_plant_health("", 6, 7)
    except ValueError as e:
        print(e)
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(e)
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)
    print("All error raising tests completed!")


test_plant_checks()
