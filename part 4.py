# Program 4: Iteration and Introspection
# Print every enum value without hardcoding; examine what happens when
# two names share the same integer value (aliasing).
# Beyond Normal Usage: Python DOES allow aliases — iteration skips them silently.

from enum import Enum

class Color(Enum):
    RED    = 1
    GREEN  = 2
    BLUE   = 3
    YELLOW = 4

# --- Normal Usage: built-in iteration ---
# Iterating a Python Enum is built in — no reflection required.
print("All Color values:")
for c in Color:
    print(f"  {c.name} = {c.value}")

# List() and len() work too
print(f"\nTotal members: {len(list(Color))}")

# --- Introspection ---
print("\nIntrospection via __members__:")
for name, member in Color.__members__.items():
    print(f"  {name!r} -> {member}")

# --- Beyond Normal Usage: two names, same integer value (aliasing) ---
# Python Enum allows this — the second name becomes an ALIAS of the first.
# Aliases do NOT appear when iterating normally; they ARE in __members__.
print("\n[Beyond Normal Usage] Enum with duplicate integer values:")

class Priority(Enum):
    LOW    = 1
    MEDIUM = 5
    HIGH   = 10
    URGENT = 10   # alias for HIGH — same value

print("Iterating Priority (aliases are hidden):")
for p in Priority:
    print(f"  {p.name} = {p.value}")

print("\nFull __members__ (aliases visible):")
for name, member in Priority.__members__.items():
    print(f"  {name!r} -> {member!r}")

print("\nIs Priority.URGENT the same object as Priority.HIGH?", Priority.URGENT is Priority.HIGH)
print("Priority(10) returns:", Priority(10))  # returns HIGH, not URGENT
print("\nConclusion:")
print("  Python silently makes URGENT an alias of HIGH.")
print("  Iteration skips aliases — only the canonical name appears.")
print("  __members__ shows all names including aliases.")
print("  Priority(10) always resolves to the FIRST name defined for that value.")