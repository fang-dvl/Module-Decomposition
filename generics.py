from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: List["Person"]

fatma = Person(name="Fatma", age=25, children=[])
aisha = Person(name="Aisha",age=30, children=[])

imran = Person(name="Imran", age=50, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)