from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class OperatingSystem(Enum):
  MACOS = "macOS"
  ARCH = "Arch Linux"
  UBUNTU = "Ubuntu"
  WINDOWS = "Windows"

@dataclass(frozen=True)
class Person:
  name: str
  age: int
  # Sorted in order of preference, most preferred is first.
  preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
  id: int
  manufacturer: str
  model: str
  screen_size_in_inches: float
  operating_system: OperatingSystem


# Calculate how sad a person will be with a given laptop
# Sadness = index position of the OS in the preference list (0 = happy, higher = less happy)
# If the OS is not in the person’s preference list, sadness = 100
def calculate_sadness(person: Person, laptop: Laptop) -> int:
  if laptop.operating_system in person.preferred_operating_system:
    return person.preferred_operating_system.index(laptop.operating_system)
  return 100


# Allocate laptops to people based on the lowest sadness score
# Each person should get exactly one laptop
# Once a laptop is assigned, it is removed from the available list
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
  allocation = {}
  remaining_laptops = laptops.copy()

  for person in people:
    # find best laptop for this person
    best_laptop = None
    best_sadness = 999

    for laptop in remaining_laptops:
      sadness = calculate_sadness(person, laptop)
      if sadness < best_sadness:
        best_sadness = sadness
        best_laptop = laptop
      
      # If sadness is 0, it means this is the perfect match, no need to check further
      if sadness == 0:
        break

    # assign and remove from pool
    if best_laptop:
      allocation[person] = best_laptop
      remaining_laptops.remove(best_laptop)

  return allocation


people = [
  Person("Fatma", 34, (OperatingSystem.UBUNTU, OperatingSystem.ARCH, OperatingSystem.MACOS)),
  Person("Eliza", 29, (OperatingSystem.ARCH, OperatingSystem.MACOS, OperatingSystem.UBUNTU)),
  Person("Lina", 27, (OperatingSystem.WINDOWS,)),
]

laptops = [
  Laptop(1, "Apple", "MacBook", 13, OperatingSystem.MACOS),
  Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
  Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]

result = allocate_laptops(people, laptops)

for person, laptop in result.items():
  print(f"{person.name} got {laptop.model} ({laptop.operating_system.value}) → sadness = {calculate_sadness(person, laptop)}")
