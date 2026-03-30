# Program 3: Extended Enum Behavior
# Python enums support associated data via custom __init__ and methods.
# Beyond Normal Usage: invoke a method on a None enum variable.

from enum import Enum
import math

class Shape(Enum):
    # Each variant carries its own tuple of dimension data.
    # The value is the first argument; extra args go to __init__.
    CIRCLE    = (5.0,)
    RECTANGLE = (3.0, 4.0)
    TRIANGLE  = (6.0, 8.0, 10.0)

    def __init__(self, *dims):
        # Store the dimensions tuple as instance data
        self.dims = dims

    def area(self) -> float:
        """Compute area based on which variant this is."""
        match self:
            case Shape.CIRCLE:
                return math.pi * self.dims[0] ** 2
            case Shape.RECTANGLE:
                return self.dims[0] * self.dims[1]
            case Shape.TRIANGLE:
                a, b, c = self.dims
                s = (a + b + c) / 2
                return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def info(self) -> str:
        return f"{self.name} -> area = {self.area():.2f}"

# --- Normal Usage ---
print("Extended enum variants with associated data:")
for shape in Shape:
    print(f"  {shape.info()}")

# --- Beyond Normal Usage: None enum variable ---
# Python has no null-safety. Setting a variable to None is always legal.
# Calling a method on None raises AttributeError at RUNTIME — no warning.
print("\n[Beyond Normal Usage] Calling .area() on None:")
null_shape = None
try:
    result = null_shape.area()   # AttributeError
    print(f"Area: {result}")
except AttributeError as e:
    print(f"  AttributeError caught at RUNTIME: {e}")
    print("  Python does NOT prevent None assignment to 'enum' variables.")
    print("  There is no compile-time check — type hints help, but are not enforced.")

# Type hint doesn't stop None either — hints are advisory only
print("\n[Beyond Normal Usage] Type-hinted variable still accepts None:")
def print_area(s: Shape) -> None:
    print(f"  Area: {s.area():.2f}")

try:
    print_area(None)  # type hint says Shape, but Python ignores it at runtime
except AttributeError as e:
    print(f"  AttributeError at RUNTIME despite type hint: {e}")