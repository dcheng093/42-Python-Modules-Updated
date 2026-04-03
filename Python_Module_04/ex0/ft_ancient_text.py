#!/usr/bin/python3.10

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        with open(filename, "r") as f:
            print("---\n")
            for line in f:
                print(line.rstrip())
            print("\n---")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}\n")
    else:
        print(f"File '{filename}' closed.")

# print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
# filename = "ancient_fragment.txt"
# print(f"Accessing Storage Vault: {filename}")
# try:
#     f = open(filename, "r")
#     print("Connection established...\n")
#     print("RECOVERED DATA:")
#     content = f.read()
#     print(content)
#     print("\nData recovery complete. Storage unit disconnected.")
# except FileNotFoundError:
#     print("ERROR: Storage vault not found. Run data generator first.")
# finally:
#     if f:
#         f.close()
