from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    # Added age
    age: int
    children: List["Person"]

fatma = Person(name="Fatma", age = 11,children=[])
aisha = Person(name="Aisha", age = 7, children=[])

imran = Person(name="Imran", age = 39, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)