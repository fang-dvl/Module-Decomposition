from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    children: List["Person"]

    @property
    def age(self) -> int:
        today = date.today()
        dob = self.date_of_birth
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def print_family_tree(person: Person, indent: int = 0) -> None:
    spacer = "  " * indent
    print(f"{spacer}{person.name} (Age: {person.age})")
    for child in person.children:
        print_family_tree(child, indent + 1)

fatma = Person(name="Fatma", date_of_birth=date(2012, 5, 14), children=[])
aisha = Person(name="Aisha", date_of_birth=date(2015, 8, 3), children=[])
imran = Person(name="Imran", date_of_birth=date(1985, 2, 20), children=[fatma, aisha])

print_family_tree(imran)