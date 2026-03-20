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
    preferred_operating_system: List[OperatingSystem]

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    laptops_remaining = laptops.copy()  
    allocation: Dict[Person, Laptop] = {}

    for person in people:
        best_laptop = None
        best_sadness = 101 

       
        for laptop in laptops_remaining:
            if laptop.operating_system in person.preferred_operating_system:
                sadness = person.preferred_operating_system.index(laptop.operating_system)
            else:
                sadness = 100

            if sadness < best_sadness:
                best_sadness = sadness
                best_laptop = laptop

        if best_laptop is None:
            raise ValueError(f"No laptops available to allocate to {person.name}")

        allocation[person] = best_laptop
        laptops_remaining.remove(best_laptop)

    return allocation