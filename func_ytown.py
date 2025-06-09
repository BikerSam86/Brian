from __future__ import annotations

"""Miscellaneous small utility functions."""

from datetime import datetime
from random import choice
from math import sqrt
import sys

def reverse_string(s: str) -> str:
    """Return the reversed version of the input string."""
    return s[::-1]


def fizzbuzz(n: int) -> list[str]:
    """Return list of FizzBuzz strings up to n (inclusive)."""
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def collatz_sequence(n: int) -> list[int]:
    """Generate Collatz sequence starting at n."""
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = int(sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def digital_root(n: int) -> int:
    """Return digital root (repeated sum of digits) of n."""
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


_QUANTUM_STATES = {"alive": "alive", "dead": "dead"}


def schrodinger_cat(state: str) -> str:
    """Quantum joke: 'alive', 'dead', or 'both' depending on input."""
    return _QUANTUM_STATES.get(state, "both")


_ELEMENTS = {
    1: "H",
    2: "He",
    3: "Li",
    4: "Be",
    5: "B",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    10: "Ne",
}


def atomic_number_to_element(num: int) -> str:
    """Return element symbol or name for atomic number."""
    return _ELEMENTS.get(num, "Unknown")


_DEF_GRAVITY = 6.67430e-11


def gravity_on_planet(mass: float, radius: float) -> float:
    """Return surface gravity in m/s^2 for planet of given mass (kg) and radius (m)."""
    return _DEF_GRAVITY * mass / (radius * radius)


_SUBSTANCE_POINTS = {
    "water": (100.0, 0.0),
    "ethanol": (78.37, -114.1),
    "mercury": (356.7, -38.83),
}


def boil_freeze_point(substance: str) -> tuple[float, float]:
    """Return (boiling point, freezing point) in °C for given substance."""
    return _SUBSTANCE_POINTS.get(substance.lower(), (float("nan"), float("nan")))


_WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def weekday_of_birthdate(date: str) -> str:
    """Given YYYY-MM-DD, return day of week."""
    dt = datetime.strptime(date, "%Y-%m-%d")
    return _WEEKDAYS[dt.weekday()]


def leap_year(year: int) -> bool:
    """Return True if year is leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def anagram_finder(word: str, words: list[str]) -> list[str]:
    """Return all anagrams of word from given list."""
    target = sorted(word)
    return [w for w in words if sorted(w) == target]


_VOWELS = "aeiouAEIOU"


def pig_latin(text: str) -> str:
    """Convert sentence to Pig Latin."""
    def translate(word: str) -> str:
        if word[0] in _VOWELS:
            return word + "yay"
        for i, ch in enumerate(word):
            if ch in _VOWELS:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

    return " ".join(translate(w) for w in text.split())


_HAIKU = [
    "An old silent pond",
    "A frog jumps into the pond",
    "Splash! Silence again.",
]


def haiku_generator() -> str:
    """Return a random 5-7-5 syllable haiku."""
    return "\n".join(_HAIKU)


_FORTUNES = [
    "You will have a pleasant surprise.",
    "Adventure awaits you today.",
    "Now is the time to try something new.",
]


def fortune_cookie() -> str:
    """Return a random fortune string."""
    return choice(_FORTUNES)


_CRAB_WORDS = ["crab", "crustacean", "decapod"]


def crabify(text: str) -> str:
    """Replace nouns in text with 'crab' or crab-themed word."""
    words = text.split()
    return " ".join(choice(_CRAB_WORDS) if w.istitle() else w for w in words)


def spiral_index(n: int) -> tuple[int, int]:
    """Return (x, y) coordinates of nth step in a spiral (starting from center)."""
    if n == 0:
        return (0, 0)
    layer = 1
    while (2 * layer - 1) ** 2 < n:
        layer += 1
    leg_len = 2 * layer - 1
    max_num = leg_len ** 2
    steps = max_num - n
    side = steps // (leg_len - 1)
    offset = steps % (leg_len - 1)
    if side == 0:
        return (layer - 1 - offset, -(layer - 1))
    if side == 1:
        return (-(layer - 1), -layer + 1 + offset)
    if side == 2:
        return (-layer + 1 + offset, layer - 1)
    return (layer - 1, layer - 1 - offset)


def turbo_encabulate(level: int) -> str:
    """Return turbo-encabulator techno-jargon for given verbosity level."""
    jargon = [
        "The turbo-encabulator provides inverse reactive current",
        "for use in unilateral phase detractors",
        "eliminating sinusoidal depleneration",
        "and producing a pre-famulated amulite",
    ]
    return " ".join(jargon[: max(1, min(level, len(jargon)))])


_SEED = 42


def crab_evolution_steps(species: str) -> int:
    """Return pseudo-random number of steps until species is a crab."""
    return (sum(ord(c) for c in species) + _SEED) % 100


def recursion_limit() -> int:
    """Return Python's current recursion limit."""
    import sys

    return sys.getrecursionlimit()


if __name__ == "__main__":
    for func in (
        reverse_string,
        fizzbuzz,
        collatz_sequence,
        is_prime,
        digital_root,
    ):
        print(func.__name__, "->", func.__doc__)

