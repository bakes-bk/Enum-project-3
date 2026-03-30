# Program 2: Exhaustive Control Flow
# Demonstrates match/case covering every enum variant (Python 3.10+).
# Beyond Normal Usage: adds a new variant without updating the match block.

from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    FALL   = 3
    WINTER = 4

def describe(season: Season) -> str:
    # Python's structural pattern matching (match/case) does NOT enforce
    # exhaustiveness at compile time — there is no compiler.
    # A missing case silently falls through; no error is raised at runtime
    # unless you explicitly add a check or raise in the wildcard arm.
    match season:
        case Season.SPRING: return "Warm and rainy"
        case Season.SUMMER: return "Hot and sunny"
        case Season.FALL:   return "Cool and breezy"
        case Season.WINTER: return "Cold and snowy"
        case _:
            # The wildcard arm (_) acts as the "default".
            # Without it, an unmatched value just returns None silently.
            raise ValueError(f"Unhandled season: {season}")

# --- Normal Usage ---
print("match/case covering all variants:")
for s in Season:
    print(f"  {s.name}: {describe(s)}")

# --- Beyond Normal Usage: add a new variant, don't update match ---
# Python lets us extend an Enum at runtime using functional syntax.
# This simulates adding MONSOON without updating describe().
print("\n[Beyond Normal Usage] Adding Season.MONSOON without updating match:")

# Functional-style enum creation lets us add a new member dynamically
ExtendedSeason = Enum("ExtendedSeason", {**{m.name: m.value for m in Season}, "MONSOON": 5})

def describe_old(season) -> str:
    """Original describe(), intentionally not updated for MONSOON."""
    match season.name:   # compare by name since it's a different class now
        case "SPRING": return "Warm and rainy"
        case "SUMMER": return "Hot and sunny"
        case "FALL":   return "Cool and breezy"
        case "WINTER": return "Cold and snowy"
        # No MONSOON case — the wildcard below fires silently
        case _:        return None  # silently returns None, no error!

result = describe_old(ExtendedSeason.MONSOON)
print(f"  describe_old(MONSOON) returned: {repr(result)}")
print("  Python does NOT warn. The missing case returns None silently.")
print("  There is no compile-time check — this is a runtime-only language.")