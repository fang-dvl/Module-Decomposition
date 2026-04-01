from dataclasses import dataclass
# Import Enum to set constant values
from enum import Enum
# Import List to specify certain variables (List[Laptop]) 
from typing import List
# Import sys module to print errors 
import sys

# Define Enum for OperatingSystems 
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

# frozen=True - makes it read-only, can't change it 
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

# Function to find laptops matching a person's preferred OS and return list with possible laptops
def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops

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

# Try block to handle possible errors
try:
    # Inputs from user
    name = input("Enter your name: ")
    age_input = input("Enter your age: ")
    age = int(age_input)
    # strip() - remove whitespaces from the start and end of the string
    os_input = input("Enter your preferred Operating System (macOS, Arch Linux or Ubuntu): ").strip()

    # Convert the string input to an OperatingSystem enum
    operating_system_map = {
        "macos": OperatingSystem.MACOS,
        "arch linux": OperatingSystem.ARCH,
        "ubuntu": OperatingSystem.UBUNTU
    }
    # It looks up the lowercase string (lower()) in operating_system_map
    preferred_os = operating_system_map.get(os_input.lower())

    # Show error, if the input os is not found 
    if preferred_os is None:
        print("Error: Invalid operating system name.", file=sys.stderr)
        sys.exit(1)
    # Create a Person object with all data 
    person = Person(name=name, age=age, preferred_operating_system=preferred_os)
    
    # Show error, if the input age is not a number
except ValueError:
    print("Error: Age must be a number!", file=sys.stderr)
    sys.exit(1)

# Find possible laptop for the user
matching_laptops = find_possible_laptops(laptops, person)
print(f"\nHi {person.name}, we found {len(matching_laptops)} laptop(s) with {preferred_os.value}.")

# Count how many laptops are available for each os
laptops_per_os = {}
for laptop in laptops:
    operating_system = laptop.operating_system
    if operating_system in laptops_per_os:
        laptops_per_os[operating_system] += 1
    else:
        laptops_per_os[operating_system] = 1

# Find which OS has the most laptops
most_available_os = None
max_laptop_count = 0
for os_name, count in laptops_per_os.items():
    if count > max_laptop_count:
        most_available_os = os_name
        max_laptop_count = count

# Print message to the user if there’s a different OS with more laptops available
if most_available_os != preferred_os and max_laptop_count > len(matching_laptops):
    print(f"If you're fine using {most_available_os.value}, there are {max_laptop_count} laptops available with that operating system")

