from dataclasses import dataclass
from enum import Enum
import sys
from typing import List, Optional
from collections import Counter

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
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops

def parse_operating_system(s: str) -> Optional[OperatingSystem]:
    s_normal = s.strip().lower()
    for os in OperatingSystem:
        if os.value.lower() == s_normal:
            return os
    return None


people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

def input_name() -> str:
    while True:
        name = input("Enter your name: ")
        if name == "":
            print("Error: Name cannot be empty. Please try again.")
        else:
            return name

def input_age() -> int:
    while True:
        try:
            age_input = input("Enter your age: ")
            age = int(age_input)
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return age
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)

def input_operating_system() -> OperatingSystem: 
    while True:
        os_input = input("Preferred operating system (macOS, Arch Linux, Ubuntu): ").strip()
        preferred_os = parse_operating_system(os_input)
        if preferred_os is not None:
            return preferred_os
        print("Please choose one of: macOS, Arch Linux, Ubuntu.")

name = input_name()
age = input_age()
preferred_os = input_operating_system()


# Create the Person with validated types 
person = Person(name=name, age=age, preferred_operating_system=preferred_os) 
people.append(person)   

# Find matching laptops and print count 
for person in people:
    matching_laptops = find_possible_laptops(laptops, person)
    print(f"\nHi {person.name}, we found {len(matching_laptops)} laptop(s) acc. your preferred OS ({person.preferred_operating_system.value}).")

# Count how many laptops exist per OS using Counter
os_counts = Counter(laptop.operating_system for laptop in laptops)

# Find OS with most available laptops
best_os = max(os_counts, key=lambda os: os_counts[os])
best_count = os_counts[best_os]

# Compare with user preferences 
preferred_count = os_counts.get(person.preferred_operating_system, 0)

if best_os != person.preferred_operating_system and best_count > preferred_count:
    print(f"\n More laptops are available if you choose {best_os.value} ({best_count} available).")          