# Program 5: Applied Enumeration — Card Game
# A small card game where Suit and Rank enums drive all game logic.
# Enums carry data and methods; removing them would require significant redesign.

from enum import Enum
import random
from dataclasses import dataclass

# --- Suit enum: carries a display symbol and trump priority ---
class Suit(Enum):
    CLUBS    = ("♣", 1)
    DIAMONDS = ("♦", 2)
    HEARTS   = ("♥", 3)
    SPADES   = ("♠", 4)

    def __init__(self, symbol: str, trump_order: int):
        self.symbol = symbol
        self.trump_order = trump_order  # higher = stronger trump suit

    def is_red(self) -> bool:
        return self in (Suit.HEARTS, Suit.DIAMONDS)

    def is_black(self) -> bool:
        return self in (Suit.CLUBS, Suit.SPADES)

# --- Rank enum: carries ordering and point values for scoring ---
class Rank(Enum):
    TWO   = (2,  2)
    THREE = (3,  3)
    FOUR  = (4,  4)
    FIVE  = (5,  5)
    SIX   = (6,  6)
    SEVEN = (7,  7)
    EIGHT = (8,  8)
    NINE  = (9,  9)
    TEN   = (10, 10)
    JACK  = (11, 10)
    QUEEN = (12, 10)
    KING  = (13, 10)
    ACE   = (14, 11)

    def __init__(self, order: int, point_value: int):
        self.order = order
        self.point_value = point_value

# --- Card: a pairing of Rank + Suit, with game logic ---
@dataclass
class Card:
    rank: Rank
    suit: Suit

    def __str__(self) -> str:
        return f"{self.rank.name}{self.suit.symbol}"

    def point_value(self) -> int:
        return self.rank.point_value

    def beats(self, other: "Card") -> bool:
        """Higher rank wins; ties broken by trump suit order."""
        if self.rank.order != other.rank.order:
            return self.rank.order > other.rank.order
        return self.suit.trump_order > other.suit.trump_order

# --- Deck: built by iterating all Suit and Rank enum values ---
def build_deck() -> list[Card]:
    deck = [Card(rank, suit) for suit in Suit for rank in Rank]
    random.shuffle(deck)
    return deck

# --- Main game ---
deck = build_deck()
print(f"Deck size: {len(deck)} cards\n")

hand_a = deck[:5]
hand_b = deck[5:10]

print("Player A hand:", [str(c) for c in hand_a])
print("Player B hand:", [str(c) for c in hand_b])

# Score each hand using Rank point values
score_a = sum(c.point_value() for c in hand_a)
score_b = sum(c.point_value() for c in hand_b)
print(f"\nPlayer A score: {score_a}")
print(f"Player B score: {score_b}")
print(f"Winner: Player {'A' if score_a >= score_b else 'B'}")

# Suit analysis driven entirely by Suit enum methods and data
print("\nSuit color analysis:")
for suit in Suit:
    print(f"  {suit.symbol} {suit.name:<9} red={str(suit.is_red()):<6} "
          f"black={str(suit.is_black()):<6} trump-order={suit.trump_order}")

# Head-to-head: best card from each hand
top_a = max(hand_a, key=lambda c: c.rank.order)
top_b = max(hand_b, key=lambda c: c.rank.order)
print(f"\nHead-to-head — best card:")
print(f"  Player A plays: {top_a}")
print(f"  Player B plays: {top_b}")
print(f"  {'Player A' if top_a.beats(top_b) else 'Player B'} wins the hand!")