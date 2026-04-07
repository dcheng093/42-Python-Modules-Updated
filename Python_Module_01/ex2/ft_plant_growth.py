#!/usr/bin/env python3.10


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow(self, cm: float) -> None:
        self.height += cm

    def age_by(self, days: int) -> None:
        self.age += days

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 24.2, 29)
    start_height: float = plant1.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ====")
        plant1.grow(0.8)
        plant1.age_by(1)
        print(plant1.show())
    total_growth: int = round(plant1.height - start_height)
    print(f"Growth this week: {total_growth}cm")

# class Plant:
#     def __init__(self, name, height, age):
#         self.name = name.capitalize()
#         self.height = height
#         self.age = age

#     def grow(self, cm):
#         self.height += cm

#     def age_by(self, days):
#         self.age += days

#     def get_info(self):
#         return (f"{self.name}: {self.height}cm, {self.age} days old")


# if __name__ == "__main__":
#     plant1 = Plant("Rose", 25, 30)
#     plant2 = Plant("Sunflower", 80, 45)
#     plant3 = Plant("Cactus", 15, 120)
#     garden = [plant1, plant2, plant3]

#     print("=== Day 1 ===")
#     for plant in garden:
#         print(plant.get_info())
#     days = 6
#     growth_per_plant = {"Rose": 6, "Sunflower": 200, "Cactus": 2}
#     for plant in garden:
#         plant.age_by(days)
#         plant.grow(growth_per_plant[plant.name])

#     print("\n=== Day 7 ===")
#     for plant in garden:
#         print(plant.get_info())
#         print(f"Growth this week: +{growth_per_plant[plant.name]}cm")
