#!/usr/bin/python3.10

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
filename = "ancient_fragment.txt"
print(f"Accessing Storage Vault: {filename}")
try:
    f = open(filename, "r")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    content = f.read()
    print(content)
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
finally:
    if f:
        f.close()
