#!/usr/bin/python3.10

def crisis_response(filename: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
        return
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
        return
    print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    with open(filename, "r") as f:
        content = f.read()
        print(f"SUCCESS: Archive recovered - ''{content}''")
        print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_response("lost_archive.txt")
    crisis_response("classified_vault.txt")
    crisis_response("standard_archive.txt")
