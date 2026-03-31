CS 31600 - Enumeration Types: Java vs Python

HOW TO RUN

Java (requires JDK 21+):
  cd java
  javac EnumBasics.java && java EnumBasics
  javac ExhaustiveControlFlow.java && java ExhaustiveControlFlow
  javac ExtendedEnumBehavior.java && java ExtendedEnumBehavior
  javac IterationIntrospection.java && java IterationIntrospection
  javac AppliedEnumeration.java && java AppliedEnumeration

Python (requires Python 3.10+):
  cd python
  python3 enum_basics.py
  python3 exhaustive_control_flow.py
  python3 extended_enum_behavior.py
  python3 iteration_introspection.py
  python3 applied_enumeration.py

FILES

  java/EnumBasics.java              - Program 1
  java/ExhaustiveControlFlow.java   - Program 2
  java/ExtendedEnumBehavior.java    - Program 3
  java/IterationIntrospection.java  - Program 4
  java/AppliedEnumeration.java      - Program 5

  python/enum_basics.py             - Program 1
  python/exhaustive_control_flow.py - Program 2
  python/extended_enum_behavior.py  - Program 3
  python/iteration_introspection.py - Program 4
  python/applied_enumeration.py     - Program 5

PROGRAMS

1. Enum Basics (Direction enum)
   Basic declaration, assignment, printing, and iteration.
   Beyond normal: values()[99] throws ArrayIndexOutOfBoundsException in Java at runtime.
   Python Direction(99) throws ValueError at runtime. IntEnum arithmetic silently returns a plain int.

2. Exhaustive Control Flow (Season enum)
   Switch/match covering all variants. WINTER deliberately left out to show each language's response.
   Java switch expression: compile-time error if a case is missing.
   Java switch statement: silently falls to default, no warning.
   Python match: silently returns None, no warning, not even at runtime.

3. Extended Enum Behavior (Shape enum with data)
   Enums carrying per-variant data (radius, sides) with an area() method.
   Beyond normal: calling .area() on null/None. Both languages crash at runtime only Java throws
   NullPointerException, Python throws AttributeError. Type hints in Python do not help.

4. Iteration and Introspection (Color and Priority enums)
   Iterating all values without hardcoding. Tests what happens when two names share the same integer.
   Java: HIGH and URGENT get different ordinals and are different objects even if .level is the same.
   Python: URGENT silently becomes an alias for HIGH. They are the same object. Iteration hides URGENT.

5. Applied Enumeration - Card Game (Suit and Rank enums)
   Full 52-card deck built by iterating both enums. Suit carries a symbol and trump order.
   Rank carries ordering and point values. Card.beats() uses enum data to compare cards.

AI was used to debug Code
