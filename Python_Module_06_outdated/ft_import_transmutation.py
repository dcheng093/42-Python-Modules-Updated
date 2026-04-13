#!/usr/bin/python3.10

import alchemy
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion
from alchemy.elements import create_earth, create_fire
print("\n=== Import Transmutation Mastery ===\n")
print("Method 1 - Full module import:\n"
      "alchemy.elements.create_fire(): "
      f"{alchemy.elements.create_fire()}\n")
print("Method 2 - Specific function import:\n"
      f"create_water(): {create_water()}\n")
print("Method 3 - Aliased import:\n"
      f"heal(): {heal()}\n")
print("Method 4 - Multiple imports:\n"
      f"create_earth(): {create_earth()}\n"
      f"create_fire(): {create_fire()}\n"
      f"strenght_potion(): {strength_potion()}\n")
print("All import transmutation methods mastered!")
