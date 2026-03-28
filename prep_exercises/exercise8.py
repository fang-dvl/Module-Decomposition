'''
Write a program which:

Already has a list of Laptops that a library has to lend out.
Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
Tells the user how many laptops the library has that have that operating system.
If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.'''

from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import Counter
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

#library’s laptops
laptops = [
    Laptop(1, "Dell", "XPS 13", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS 15", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Lenovo", "ThinkPad", 14, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook Air", 13, OperatingSystem.MACOS),
]
#user input
name = input("Enter your name: ").strip()
try:
    age = int(input("Enter your age: ").strip())
except ValueError:
    print("Error Age must be a number ", file=sys.stderr)
    sys.exit(1)
os_input = input("Enter your preferred operating system (macOS / Arch Linux / Ubuntu): ").strip()
try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print(f"Error '{os_input}' is not a valid operating system.", file=sys.stderr)
    print("Valid options are:", [os.value for os in OperatingSystem], file=sys.stderr)
    sys.exit(1)

#Processing
person = Person(name=name, age=age, preferred_operating_system=preferred_os)
matching_laptops = [l for l in laptops if l.operating_system == person.preferred_operating_system]

print(f"\n library has {len(matching_laptops)} laptop/s with {preferred_os.value}")

#suggest an alternative if better availability
os_counts = Counter([l.operating_system for l in laptops])
most_common_os, most_common_count = os_counts.most_common(1)[0]

if most_common_os != preferred_os and most_common_count > len(matching_laptops):
    print(f"💡 There are more laptops with {most_common_os.value}.")
    print(f"If you’re willing to use {most_common_os.value}, you’re more likely to get one.")