#!/usr/bin/python3.10

from math import sqrt


def distance_between(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def get_player_pos() -> tuple:
    while True:
        try:
            user_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            parts = user_input.split(",")
            if len(parts) != 3:
                raise ValueError("Wrong number of values")
            coords = []
            for part in parts:
                try:
                    coords.append(float(part.strip()))
                except ValueError as e:
                    print(f"Error on parameter '{part.strip()}': {e}")
                    break
            else:
                return tuple(coords)
        except ValueError:
            print("Invalid syntax")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x, y, z = pos1
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {distance_between((0, 0, 0), pos1):.4f}")
    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{distance_between(pos1, pos2):.4f}"
    )

# def parse_coords(coord_str):
#     try:
#         x_str, y_str, z_str = coord_str.split(',')
#         return (int(x_str), int(y_str), int(z_str))
#     except Exception as e:
#         print(f"Error parsing coordinates: {e}")
#         print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
#         return None


# def show_unpacking(position):
#     x, y, z = position
#     print(f"Player at x={x}, y={y}, z={z}")
#     print(f"Coordinates: X={x}, Y={y}, Z={z}")


# if __name__ == "__main__":
#     print("=== Game Coordinate System ===\n")
    # pos1 = (10, 20, 5)
    # origin = (0, 0, 0)
    # print(f"Position created: {pos1}")
    # print(f"Distance between {origin} and {pos1}: "
    #       f"{distance_between(origin, pos1):.2f}\n")
    # parsed = "3,4,0"
    # print(f'Parsing coordinates: "{parsed}"')
    # print(f"Parsed position: {parse_coords(parsed)}")
    # print(f"Distance between {origin} and {parse_coords(parsed)}: "
    #       f"{distance_between(origin, parse_coords(parsed))}\n")
    # invalid = "abc,def,ghi"
    # print(f'Parsing invalid coordinates: "{invalid}"')
    # parse_coords(invalid)
    # print("\nUnpacking demonstration:")
    # parsed_pos = parse_coords(parsed)
    # show_unpacking(parsed_pos)
