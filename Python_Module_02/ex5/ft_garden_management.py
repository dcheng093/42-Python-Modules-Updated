#!/usr/bin/python3.10

class EmptyNameError(Exception):
    pass


class NegativeWater(Exception):
    pass


class HealthError(Exception):
    pass


class EmptyTankError(Exception):
    pass


class Plant:

    def __init__(self, name, water=0, sun=0):
        self.name = name
        self.water = water
        self.sun = sun

    def check_health(self):
        if self.water < 1 or self.water > 10:
            raise HealthError(
                f"Error checking {self.name}: Water level {self.water} is too "
                f"{'low (min 1)' if self.water < 1 else 'high (max 10)'}\n"
            )
        elif self.sun < 2 or self.sun > 12:
            raise HealthError(
                f"Error checking {self.name}: Sunlight level {self.sun} is too"
                f"{' low (min 2)' if self.sun < 2 else ' high (max 12)'}\n"
            )
        else:
            print(f"{self.name}: healthy "
                  f"(water: {self.water}, sun: {self.sun})")


class GardenManager:

    def __init__(self):
        self.__plants = []

    def add_plant(self, plant):
        try:
            if not plant.name:
                raise EmptyNameError("Error adding plant: Plant name "
                                     "cannot be empty!")
            else:
                print(f"Added {plant.name} successfully")
                self.__plants = self.__plants + [plant]
        except Exception as e:
            print(e)

    def water_plants(self, amount, water_level):
        try:
            if amount < 0:
                raise NegativeWater("Error watering plant: Negative amount")
            else:
                for plant in self.__plants:
                    if amount > water_level:
                        raise EmptyTankError("Not enough water in tank")
                    plant.water += amount
                    water_level -= amount
                    print(f"Watering {plant.name} - success")
        except Exception:
            raise

    def check_health(self):
        print("Checking plant health...")
        if len(self.__plants) == 0:
            print("List of plants is empty.")
        else:
            try:
                for plant in self.__plants:
                    plant.check_health()
            except Exception as e:
                print(e)


def test_garden_management():
    print("=== Garden Management System ===")
    manager = GardenManager()
    print("\nAdding plants to garden...")
    manager.add_plant(Plant("tomato", 2, 8))
    manager.add_plant(Plant("lettuce", 12, 2))
    manager.add_plant(Plant("", water=5, sun=5))
    print("")
    print("Watering plants...")
    print("Opening watering system")
    manager.water_plants(amount=3, water_level=10)
    print("Closing watering system (cleanup)")
    print("")
    manager.check_health()
    print("Testing error recovery...")
    try:
        manager.water_plants(amount=5, water_level=2)
    except Exception as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
