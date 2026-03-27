from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    birth_year: int
    children: List["Person"]

    @property
    def age(self) -> int:
        current_year = date.today().year
        return current_year - self.birth_year

fatma = Person(name="Fatma", birth_year=2018, children=[])
aisha = Person(name="Aisha", birth_year=2020, children=[])
imran = Person(name="Imran", birth_year=1990, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(f"{person.name} ({person.age})")
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)
