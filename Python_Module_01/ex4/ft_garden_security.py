#!/usr/bin/python3.10

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name.capitalize()
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}: {float(self.__height)}cm, "
              f"{self.__age} days old\n")

    def get_height(self):
        return self.__height

    def set_height(self, value: int):
        if value >= 0:
            self.__height = value
            print(f"Height updated: {value}cm")
        else:
            print(f"{self.__name}: Error, height can't be negative\n"
                  "Height update rejected")

    def get_age(self):
        return self.__age

    def set_age(self, value: int):
        if value >= 0:
            self.__age = value
            print(f"Age updated: {value} days\n")
        else:
            print(f"{self.__name}: Error, age can't be negative\n"
                  "Age update rejected")

    def show(self):
        print(
            f"\nCurrent state: {self.__name}: "
            f"{float(self.__height)}cm, {self.__age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 15, 10)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-10000000000)
    plant.set_age(-10000000000)
    plant.show()
