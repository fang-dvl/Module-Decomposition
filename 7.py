from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: List[str]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_systems: List[str]


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_systems == person.preferred_operating_systems:
            possible_laptops.append(laptop)
    return possible_laptops

people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_systems=["Arch Linux"]),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_systems=["Ubuntu"]),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_systems=["ubuntu"]),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_systems=["macOS"]),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")