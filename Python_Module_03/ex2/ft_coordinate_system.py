#!/usr/bin/python3.10

import math


def distance_between(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coords(coord_str):
    try:
        x_str, y_str, z_str = coord_str.split(',')
        return (int(x_str), int(y_str), int(z_str))
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def show_unpacking(position):
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    pos1 = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {pos1}")
    print(f"Distance between {origin} and {pos1}: "
          f"{distance_between(origin, pos1):.2f}\n")
    parsed = "3,4,0"
    print(f'Parsing coordinates: "{parsed}"')
    print(f"Parsed position: {parse_coords(parsed)}")
    print(f"Distance between {origin} and {parse_coords(parsed)}: "
          f"{distance_between(origin, parse_coords(parsed))}\n")
    invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid}"')
    parse_coords(invalid)
    print("\nUnpacking demonstration:")
    parsed_pos = parse_coords(parsed)
    show_unpacking(parsed_pos)
