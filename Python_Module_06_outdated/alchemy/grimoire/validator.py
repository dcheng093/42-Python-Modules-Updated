def validate_ingredients(ingredients: str) -> str:
    validate_ingredients = ("fire", "water", "earth", "air")
    if any(ingredient in ingredients for ingredient in validate_ingredients):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
