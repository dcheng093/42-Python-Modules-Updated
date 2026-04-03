#!/usr/bin/env python3.10


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        if self.age == 1:
            print(f"Created: {self.name}: {float(self.height)}cm,"
                  f" {self.age} day old")
        elif self.age > 1:
            print(f"Created: {self.name}: {float(self.height)}cm,"
                  f" {self.age} days old")
        else:
            print("dude it doesn't even exist")


if __name__ == "__main__":
    plants: list = [Plant("Rose", 25, 30),
                    Plant("Oak", 200, 365),
                    Plant("Cactus", 5, 90),
                    Plant("Sunflower", 80, 45),
                    Plant("Fern", 15, 120)]
    print("=== Plant Factory Output ===")
    count: int = 0
    for plant in plants:
        plant.show()

# class Plant:
#     def __init__(self, name, height, age):
#         self.name = name.capitalize()
#         self.height = height
#         self.age = age

#     def display(self):
#         print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


# if __name__ == "__main__":
#     plants = [Plant("Rose", 25, 30),
#               Plant("Oak", 200, 365),
#               Plant("Cactus", 5, 90),
#               Plant("Sunflower", 80, 45),
#               Plant("Fern", 15, 120)]
#     print("=== Plant Factory Output ===")
#     count = 0
#     for plant in plants:
#         plant.display()
#         count += 1
#     print(f"\nTotal plants created: {count}")
