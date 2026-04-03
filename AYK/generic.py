from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    children: List["Person"]
    age : int
    

fatma = Person(name="Fatma", children=[],age = 4)
aisha = Person(name="Aisha", children=[],age =2)

imran = Person(name="Imran", children=[fatma, aisha],age=33)

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)