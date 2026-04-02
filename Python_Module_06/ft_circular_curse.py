#!/usr/bin/python3.10

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell

print("\n=== Circular Curse Breaking ===\n")
print("Testing ingredient validation:")
print('validate_ingredients("fire air"): '
      f'{validate_ingredients("fire air")}\n'
      'validate_ingredients("dragon_scales"): '
      f'{validate_ingredients("dragon_scales")}\n')
print("Testing spell recording with validation:")
print('record_spell("Fireball", "fire air): '
      f'{record_spell("Fireball", "fire air")}\n'
      'record_spell("Dark Magic", "shadow"): '
      f'{record_spell("Dark Magic", "shadow")}\n')
print("Testing late import technique:")
print('record_spell("Lightning", "air"): '
      f'{record_spell("Lightning", "air")}\n')
print("Circular dependency curse avoided using late imports!\nAll spells"
      " processed safely!")
