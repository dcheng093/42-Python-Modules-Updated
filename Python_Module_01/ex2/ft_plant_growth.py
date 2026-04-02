#!/usr/bin/env python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        self.height += cm

    def age_by(self, days: int) -> None:
        self.age += days

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 24.2, 29)
    start_height: int = plant1.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ====")
        plant1.grow(0.8)
        plant1.age_by(1)
        print(plant1.show())
    total_growth: int = round(plant1.height - start_height)
    print(f"Growth this week: {total_growth}cm")
