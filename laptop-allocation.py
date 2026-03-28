from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple, Optional


# This is a list of possible operating systems for laptops
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


# This is a person who wants a laptop
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Each person has a list of operating systems they like, ordered by preference
    preferred_operating_system: Tuple[OperatingSystem, ...]


# This is a laptop with an ID and other details
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


# This function checks how much a person will dislike a laptop
# Lower number = happier, 100 = very unhappy
def calculate_sadness(person: Person, laptop: Laptop) -> int:
    try:
        # Find the position of the laptop's OS in the person's preference list
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        # If the OS is not in the list, return 100 (very sad)
        return 100 


# This function gives laptops to people based on what makes them happiest
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    allocation: Dict[Person, Laptop] = {}
    # Make a copy of the laptop list so we can remove laptops when they are taken
    available_laptops = laptops.copy()

    # Go through each person
    for person in people:
        best_laptop: Optional[Laptop] = None
        lowest_sadness = float('inf')  # Start with a very high sadness

        # Check each available laptop to find the best match
        for laptop in available_laptops:
            sadness = calculate_sadness(person, laptop)
            # If this laptop makes the person less sad than others, remember it
            if sadness < lowest_sadness:
                lowest_sadness = sadness
                best_laptop = laptop

        # If we found a good laptop, give it to the person and remove it from the list
        if best_laptop:
            allocation[person] = best_laptop
            available_laptops.remove(best_laptop)

    return allocation


# Test the program with some people and laptops
if __name__ == "__main__":
    people = [
        Person("Imran", 22, (OperatingSystem.UBUNTU, OperatingSystem.ARCH)),
        Person("Eliza", 34, (OperatingSystem.ARCH, OperatingSystem.MACOS))
    ]

    laptops = [
        Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
        Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
        Laptop(3, "Apple", "MacBook", 13, OperatingSystem.MACOS)
    ]

    allocation = allocate_laptops(people, laptops)

    # Print the result
    for person, laptop in allocation.items():
        print(f"{person.name} gets Laptop #{laptop.id} with {laptop.operating_system.value}")
