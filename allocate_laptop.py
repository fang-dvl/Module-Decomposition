from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]

    def __hash__(self):
        return hash((self.name, self.age, tuple(self.preferred_operating_system)))    



@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Optional[Laptop]]: 
    allocations: Dict[Person,  Optional[Laptop]] = {}
    available_laptops = laptops.copy()
    
    for person in people:
        allocated = None
        for preferred_os in person.preferred_operating_system:
            for laptop in available_laptops:
                if laptop.operating_system == preferred_os:
                    allocated = laptop
                    break
            if allocated:
                break
        
        if allocated:
            
            allocations[person] = allocated
            available_laptops.remove(allocated) 
        else:
            # No laptops left, assign None or a “dummy” Laptop with sadness 100
            allocations[person] = None 
    
    return allocations  


def calculate_sadness(person: Person, laptop: Optional[Laptop]) -> int:
    """Return sadness for a person if given this laptop."""
    if laptop is None:
        return 100  # no laptop, maximum sadness
    try:
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        return 100  # OS not in preferences
        
    
# Sample laptops
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

# Sample people with preferences
people = [
    Person(name="Alice", age=25, preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
    Person(name="Bob", age=30, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.ARCH]),
    Person(name="Charlie", age=22, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU]),
    Person(name="Jack", age=18, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU]),
    Person(name="Faith", age=23, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU]),
]

# Allocate laptops
allocations = allocate_laptops(people, laptops)

# Calculate total sadness
total_sadness = sum(calculate_sadness(person, laptop) for person, laptop in allocations.items())
print(f"\nTotal sadness: {total_sadness}")

# Print allocations and sadness
for person, laptop in allocations.items():
    if laptop is not None:
        print(f"{person.name} got {laptop.manufacturer} {laptop.model} ({laptop.operating_system.value}) "
            f"→ Sadness: {calculate_sadness(person, laptop)}")
    else:
        print(f"{person.name} got no laptop → Sadness: 100")