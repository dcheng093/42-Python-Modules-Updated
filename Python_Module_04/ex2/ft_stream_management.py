#!/usr/bin/python3.10

import sys


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
id = input("Input Stream active. Enter archivist ID: ")
stat_rep = input("Input Stream active. Enter status report: ")
print("")
print("{[}STANDARD{]} Archive status "
      f"from {id}: {stat_rep}", file=sys.stdout)
print("{[}ALERT{]} System diagnostic: Communication channels verified",
      file=sys.stderr)
print("{[}STANDARD{]} Data transmission complete\n")
print("Three-channel communication test successful.")
