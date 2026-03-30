# Program 1: Enumeration Basics
# Demonstrates basic enum declaration, variable assignment, and printing.
# Beyond Normal Usage: assigns an integer outside the defined enum range.

from enum import Enum

# Python's enum module was added in Python 3.4 (2013).
# Enum members have a .name (string) and a .value (assigned integer, 1-based by default).
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4

# --- Normal Usage ---
d = Direction.NORTH
print(f"Assigned direction: {d}")
print(f"Name:  {d.name}")
print(f"Value: {d.value}")

print("\nAll Direction values:")
for direction in Direction:
    print(f"  {direction.name} -> value {direction.value}")

# --- Beyond Normal Usage ---
# Python's Enum does NOT let you index by an out-of-range integer by default —
# it raises a ValueError at runtime. There is NO compile-time check.
print("\n[Beyond Normal Usage] Attempting Direction(99):")
try:
    bad = Direction(99)       # 99 is not a valid value
    print(f"Got: {bad}")
except ValueError as e:
    print(f"  ValueError caught: {e}")
    print("  Python catches this at RUNTIME only.")

# IntEnum is a subclass that *does* allow mixing with plain ints.
# This can silently accept unexpected integers.
from enum import IntEnum

class DirectionInt(IntEnum):
    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4

print("\n[Beyond Normal Usage] IntEnum arithmetic (potential silent failure):")
result = DirectionInt.NORTH + 10   # evaluates to plain int 11, no error
print(f"  NORTH + 10 = {result} (type: {type(result).__name__})")
print("  IntEnum silently returns a plain int — the enum type is lost.")