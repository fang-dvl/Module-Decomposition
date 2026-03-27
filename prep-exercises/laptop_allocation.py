from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    # Using tuple instead of List to make Person hashable (for dict keys)
    preferred_operating_system: tuple[OperatingSystem, ...]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def calculate_sadness(person: Person, laptop: Laptop) -> int:
    """Calculate sadness score for a person-laptop pairing."""
    try:
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        return 100


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    """
    Allocate laptops to people minimizing total sadness.
    
    Sadness is defined as:
    - Index in preference list (0 for first choice, 1 for second, etc.)
    - 100 if the OS is not in their preference list
    """
    if len(people) != len(laptops):
        raise ValueError("Number of people must equal number of laptops")
    
    allocation: Dict[Person, Laptop] = {}
    available_laptops = set(laptops)  # Use set for O(1) lookup and removal
    
    # Helper to find best available laptop for a person
    def find_best_available(person: Person) -> tuple[Laptop, int] | None:
        """Returns (best_laptop, sadness) or None if no laptops available."""
        best_laptop = None
        best_sadness = float('inf')
        
        for laptop in available_laptops:
            sadness = calculate_sadness(person, laptop)
            if sadness < best_sadness:
                best_sadness = sadness
                best_laptop = laptop
                # Early exit if we found a perfect match (sadness 0)
                if sadness == 0:
                    break
        
        return (best_laptop, best_sadness) if best_laptop else None
    
    # Sort people by how limited their good options are
    # (by counting how many laptops match their preferences - less matches = higher priority)
    def count_good_matches(person: Person) -> int:
        """Count how many laptops have sadness < 100 (i.e., OS is in their preferences)."""
        return sum(1 for laptop in laptops if calculate_sadness(person, laptop) < 100)
    
    sorted_people = sorted(people, key=count_good_matches)
    
    # Greedy allocation: for each person, find their best available laptop
    for person in sorted_people:
        result = find_best_available(person)
        if result:
            laptop, _ = result
            allocation[person] = laptop
            available_laptops.remove(laptop)  # O(1) removal
    
    return allocation


def calculate_total_sadness(allocation: Dict[Person, Laptop]) -> int:
    """Calculate total sadness for an allocation."""
    return sum(calculate_sadness(person, laptop) for person, laptop in allocation.items())


# Test the function
people = [
    Person("Alice", 25, (OperatingSystem.UBUNTU, OperatingSystem.ARCH, OperatingSystem.MACOS)),
    Person("Bob", 30, (OperatingSystem.MACOS, OperatingSystem.UBUNTU)),
    Person("Charlie", 28, (OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
]

laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.UBUNTU),
    Laptop(2, "Apple", "MacBook", 13, OperatingSystem.MACOS),
    Laptop(3, "Lenovo", "ThinkPad", 14, OperatingSystem.ARCH),
]

allocation = allocate_laptops(people, laptops)

print("Laptop Allocation:")
total_sadness = 0
for person, laptop in allocation.items():
    sadness = calculate_sadness(person, laptop)
    total_sadness += sadness
    print(f"{person.name} -> {laptop.manufacturer} {laptop.model} ({laptop.operating_system.value}) - Sadness: {sadness}")

print(f"\nTotal Sadness: {total_sadness}")

