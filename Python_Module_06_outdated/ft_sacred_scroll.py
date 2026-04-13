#!/usr/bin/python3.10

import alchemy

print("\n=== Scared Scroll Memory ===\n")
print("Testing direct module access:")
print("alchemy.elements.create_fire(): "
      f"{alchemy.elements.create_fire()}\n"
      "alchemy.elements.create_water(): "
      f"{alchemy.elements.create_water()}\n"
      "alchemy.elements.create_earth(): "
      f"{alchemy.elements.create_earth()}\n"
      "alchemy.elements.create_air(): "
      f"{alchemy.elements.create_air()}\n")
print("Testing package-level access (controlled by __init__.py):")
print(f"alchemy.create_fire(): {alchemy.create_fire()}\n"
      f"alchemy.create_water(): {alchemy.create_water()}")
try:
    f"alchemy.create_earth(): {alchemy.create_earth()}"
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")
try:
    f"alchemy.create_air(): {alchemy.create_air()}\n"
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed\n")
print("Package metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
