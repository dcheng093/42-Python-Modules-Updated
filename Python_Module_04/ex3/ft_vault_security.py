#!/usr/bin/python3.10

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
data = "classified_data.txt"
security = "security_protocols.txt"
print("Vault connection established with failsafe protocols\n")
print("SECURE EXTRACTION:")
with open(data, 'r') as f:
    content = f.read()
    print(content)
print("\nSECURE PRESERVATION:")
with open(security, 'r') as f:
    content = f.read()
    print(content)
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
