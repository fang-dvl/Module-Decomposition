from dataclasses import dataclass
from enum import Enum
# Optional - value can be a specific type or none 
from typing import List, Dict, Optional

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
    
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
    
# Allocate one laptop to each person based on person's preferences
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[str, Optional[Laptop]]:
    # Create an empty dictionary to store laptop is given to each person. Where key - person's name(string), the value - laptop or none
    allocation: Dict[str, Optional[Laptop]] = {}
    # Make a copy of the laptop list to safely change it and keep the original 
    available_laptops = laptops.copy()

    # Assign the laptop through going each person.
    for person in people:
        # Start with no laptop assigned 
        assigned_laptop = None
        
        # Loop through to find a laptop with os that person prefers 
        for preferred_os in person.preferred_operating_system:
            for laptop in available_laptops:
                if laptop.operating_system == preferred_os:
                    # If we find pereferred laptop, then break - stop looping through
                    assigned_laptop = laptop
                    break
            if assigned_laptop:
                break
        # If we did not find assigned laptop, assign the first available laptop 
        if not assigned_laptop and available_laptops:
            assigned_laptop = available_laptops[0]
        
        # Save the assigned laptop 
        allocation[person.name] = assigned_laptop
        if assigned_laptop:
            available_laptops.remove(assigned_laptop)
   
    return allocation
# Calculate sadness of person, it depends if we can find preferred os and laptop. If laptop is not in a list, return 100.
def sadness(person: Person, laptop: Optional[Laptop]) -> int:   
    if laptop is None:
        return 100
    try:
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        return 100

# Create a list of instances from Person class 
people = [
    Person(name="Peter", age=33, preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    Person(name="Alex", age=26, preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.ARCH]),
    Person(name="Tom", age=35, preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU]),
    ]
# Create a list of instances of Laptop class 
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=3, manufacturer="Asus", model="ZenBook", screen_size_in_inches=14, operating_system=OperatingSystem.MACOS),
]

# Call the allocate_laptops function to allocate a laptop to each person 
allocation = allocate_laptops(people, laptops)

# Loop through people to print a message if a laptop is assigned to them.
# If a laptop is assigned and the person got what they wanted, sadness is 0.
# If no laptop is assigned, sadness is 100.
for person in people:
    assigned_laptop = allocation[person.name]
    if assigned_laptop:
        print(f"{person.name} got a {assigned_laptop.manufacturer} {assigned_laptop.model} " f"with {assigned_laptop.operating_system.value}. Sadness level: {sadness(person, assigned_laptop)}")
    else:
        print(f"{person.name} did not get a laptop. Sadness level: 100")
            