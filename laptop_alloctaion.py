from dataclasses import dataclass
from enum import Enum
from typing import List


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


laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]
users = [
    Person(
        name="Andrei",
        age=20,
        preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU],
    ),
    Person(
        name="Eyuel",
        age=20,
        preferred_operating_system=[
            OperatingSystem.MACOS,
            OperatingSystem.UBUNTU,
            OperatingSystem.ARCH,
        ],
    ),
    Person(
        name="Priscilla",
        age=30,
        preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU],
    ),
    Person(
        name="Miki",
        age=21,
        preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU],
    ),
]

sadness = 0


def allocate_laptops(
    people: List[Person], laptops: List[Laptop]
) -> dict[Person, Laptop]:
    allocation = {}
    global sadness
    laptops_copy = laptops.copy()
    for person in people:
        for index in range(len(person.preferred_operating_system)):
            if person in allocation:
                break
            for laptop in laptops_copy:
                if laptop.operating_system == person.preferred_operating_system[index]:
                    allocation[person] = laptop
                    laptops_copy.remove(laptop)
                    sadness += index
                    break
        # If after distribution person still doesn't have a laptop, give him the first we can find
        if person not in allocation:
            allocation[person] = laptops[0]
            sadness += 100

    return allocation


allocation = allocate_laptops(users, laptops)
print("\n".join(f"{key} :\n {value}" for key, value in allocation.items()))
print(sadness)
