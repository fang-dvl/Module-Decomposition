from dataclasses import dataclass
from enum import Enum
from typing import List, Dict


# Define possible operating systems
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


# Define Person and Laptop
@dataclass
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]


@dataclass
class Laptop:
    id: int
    manufacturer: str
    model: str
    operating_system: OperatingSystem


# Function to calculate sadness
def sadness_for_person(person: Person, laptop: Laptop) -> int:
    """How sad a person is with this laptop."""
    if laptop.operating_system in person.preferred_operating_system:
        return person.preferred_operating_system.index(laptop.operating_system)
    else:
        return 100  # Very sad if OS not in their list


# Simple laptop allocation
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[str, Laptop]:
    """
    Give each person one laptop.
    Try to reduce sadness.
    """
    allocated = {}
    available_laptops = laptops.copy()

    for person in people:
        best_laptop = None
        best_sadness = 999

        # Try to find the best laptop for this person
        for laptop in available_laptops:
            s = sadness_for_person(person, laptop)
            if s < best_sadness:
                best_sadness = s
                best_laptop = laptop

        # Give them the best one we found
        allocated[person.name] = best_laptop
        available_laptops.remove(best_laptop)

    return allocated


# Testing data
def main():
    laptops = [
        Laptop(1, "Dell", "XPS 13", OperatingSystem.ARCH),
        Laptop(2, "Dell", "XPS 15", OperatingSystem.UBUNTU),
        Laptop(3, "Apple", "MacBook Air", OperatingSystem.MACOS),
        Laptop(4, "Dell", "Inspiron", OperatingSystem.UBUNTU),
    ]

    people = [
        Person("Imran", 22, [OperatingSystem.UBUNTU, OperatingSystem.ARCH, OperatingSystem.MACOS]),
        Person("Eliza", 34, [OperatingSystem.ARCH, OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
        Person("Sam", 29, [OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person("Tariq", 25, [OperatingSystem.ARCH]),
    ]

    allocations = allocate_laptops(people, laptops)

    print("=== Laptop Allocations ===")
    total_sadness = 0
    for name, laptop in allocations.items():
        person = next(p for p in people if p.name == name)
        sad = sadness_for_person(person, laptop)
        total_sadness += sad
        print(f"{name} gets {laptop.model} ({laptop.operating_system.value}) - sadness {sad}")

    print(f"\nTotal sadness: {total_sadness}")


if __name__ == "__main__":
    main()
