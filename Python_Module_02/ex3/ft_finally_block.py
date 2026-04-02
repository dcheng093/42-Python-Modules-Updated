#!/usr/bin/python3.10

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    plants = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plants)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    plants = ["tomato", None, "carrots"]
    plants[1]
    water_plants(plants)
    print("")
    print("Cleanup always happens, even with errors!")


test_watering_system()
