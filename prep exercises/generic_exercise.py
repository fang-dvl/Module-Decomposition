from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass(frozen=True)

class Person:
    name: str
    children: List["Person"]
    date_of_birth: str

    def person_age(self) -> int:
        today_date = date.today()
        birth_date = date.fromisoformat(self.date_of_birth)
        age = today_date.year - birth_date.year

        if (today_date.month, today_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    

fatma = Person(name="Fatma", children=[], date_of_birth="2010-06-15")
aisha = Person(name="Aisha", children=[], date_of_birth="2012-09-20")

imran = Person(name="Imran", children=[fatma, aisha], date_of_birth="1998-10-16")

def print_family_tree(person: Person) -> None:
    print(f"{person.name} (Age: {person.person_age()})")
    
    for child in person.children:
        print(f"- {child.name} ({child.person_age()})")

print_family_tree(imran)