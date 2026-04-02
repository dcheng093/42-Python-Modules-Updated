#!/usr/bin/python3.10

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def display(self):
        print(f"{self.name} ({self.__class__.__name__}):", end=" ")
        print(f"{self.height}cm, {self.age} days", end="")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def display(self):
        super().display()
        print(f", {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter

    def display(self):
        super().display()
        print(f", {self.diameter} diameter")

    def produce_shade(self):
        shade = int(self.diameter * 3.14 / 2)
        print(f"{self.name} provides {shade}", end=" ")
        print("square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self):
        super().display()
        print(f", {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


print("=== Garden Plant Types ===\n")
flower = Flower("Rose", 25, 30, "red")
flower.display()
flower.bloom()
tree = Tree("Oak", 500, 1825, 50)
tree.display()
tree.produce_shade()
vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
vegetable.display()
