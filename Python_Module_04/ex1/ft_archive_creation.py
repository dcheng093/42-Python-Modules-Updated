#!/usr/bin/python3.10

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
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
        print(f"Error opening file '{filename}': {e}")
        sys.exit(1)
    else:
        print(f"File '{filename}' closed.")
    print("Transform data:")
    transformed = [line + "#" for line in content_lines]
    print("---")
    for line in transformed:
        print(line)
    print("---")
    new_file = input("Enter new file name (or empty): ").strip()
    if new_file:
        try:
            with open(new_file, "w") as f:
                for line in transformed:
                    f.write(line + "\n")
            print(f"Saving data to '{new_file}'")
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            print(f"Error saving file '{new_file}': {e}")
    else:
        print("Not saving data.")

# print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
# newfile = "new_discovery.txt"
# print(f"Initializing new storage unit: {newfile}")
# try:
#     f = open(newfile, "w")
#     print("Storage unit created successfully...\n")
#     print("Inscribing preservation data...")
#     content = ("[ENTRY 001] New quantum algorithm discovered\n" +
#                "[ENTRY 002] Efficiency increased by 347%\n" +
#                "[ENTRY 003] Archived by Data Archivist trainee")
#     f.write(content)
#     print(content)
#     print("\nData inscription complete. Storage unit sealed.")
#     print(f"Archive '{newfile}' ready for long-term preservation.")
# except Exception as e:
#     print(e)
# finally:
#     if f:
#         f.close()
