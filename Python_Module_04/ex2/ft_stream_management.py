#!/usr/bin/python3.10

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    content_lines = []
    try:
        with open(filename, "r") as f:
            print("---\n")
            for line in f:
                line = line.rstrip()
                print(line)
                content_lines.append(line)
            print("\n---")
    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        sys.exit(1)
    else:
        print(f"File '{filename}' closed.")
    print("Transform data:")
    transformed = [line + "#" for line in content_lines]
    print("---\n")
    for line in transformed:
        print(line)
    print("\n---")
    print("Enter new file name (or empty): ", end="", flush=True)
    new_file = sys.stdin.readline().strip()
    if new_file:
        try:
            with open(new_file, "w") as f:
                for line in transformed:
                    f.write(line + "\n")
            print(f"Saving data to '{new_file}'")
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            print(f"[STDERR] Error opening file '{new_file}': {e}",
                  file=sys.stderr)
            print("Data not saved.")
    else:
        print("Not saving data.")

# print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
# id = input("Input Stream active. Enter archivist ID: ")
# stat_rep = input("Input Stream active. Enter status report: ")
# print("")
# print("{[}STANDARD{]} Archive status "
#       f"from {id}: {stat_rep}", file=sys.stdout)
# print("{[}ALERT{]} System diagnostic: Communication channels verified",
#       file=sys.stderr)
# print("{[}STANDARD{]} Data transmission complete\n")
# print("Three-channel communication test successful.")
