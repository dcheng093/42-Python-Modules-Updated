#!/usr/bin/python3.10

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name.capitalize()}: {float(self.height)}cm, {self.age} "
              "days old")


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
        print("=== Flower")

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!\n")

    def bloom(self):
        print(f"[asking the {(self.name).lower()} to bloom]")
        self.bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.diameter = trunk_diameter
        print("=== Tree")

    def show(self):
        super().show()
        print(f" Trunk diameter: {float(self.diameter)}cm")

    def produce_shade(self):
        print(f"[asking the {(self.name).lower()} to produce shade]"
              f"\n{self.__class__.__name__} {self.name.capitalize()}"
              f" now produces a shade of {float(self.height)}cm long"
              f" and {float(self.diameter)}cm wide.\n")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print("=== Vegetable")

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, cm):
        self.height += cm

    def set_age(self, days):
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        self.age += days
        self.nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    # flour
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()

    # tree
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.produce_shade()

    # veggie
    vegetable = Vegetable("Tomato", 5, 10, "April", 0)
    vegetable.show()
    vegetable.grow(42)
    vegetable.set_age(20)
    vegetable.show()
