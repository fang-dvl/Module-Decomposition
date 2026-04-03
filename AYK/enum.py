from dataclasses import dataclass
from enum import Enum
from typing import List
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    return [laptop for laptop in laptops if laptop.operating_system == person.preferred_operating_system]


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


name = input("Enter your name: ").strip()
age_input = input("Enter your age: ").strip()
age = int(age_input)
if age <= 0:
    print("Age must be positive")
    print("Available Operating Systems: macOS, Arch Linux, Ubuntu")
    os_input = input("Enter your preferred operating system: ").strip().lower()

   
    os_map = {os.value.lower(): os for os in OperatingSystem}
    if os_input not in os_map:
        print(f"Invalid operating system '{os_input}'")
    preferred_os = os_map[os_input]


    sys.exit(1)


person = Person(name=name, age=age, preferred_operating_system=preferred_os)


matching_laptops = find_possible_laptops(laptops, person)
print(f"\nHello {person.name}! There are {len(matching_laptops)} laptop(s) with {person.preferred_operating_system.value} available.")


os_counts = {os: 0 for os in OperatingSystem}
for laptop in laptops:
    os_counts[laptop.operating_system] += 1


max_os = None
max_count = 0

for os, count in os_counts.items():
    if count > max_count:
        max_os = os
        max_count = count

if max_os != person.preferred_operating_system and max_count > len(matching_laptops):
    print(f"Tip: There are more laptops available with {max_os.value}.")