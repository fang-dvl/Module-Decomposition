from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    children: List["Person"]
    
    def age(self) -> int:
        current_date = date.today()
        age = current_date.year - self.date_of_birth.year - (
            (current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
        return age

# Calculate dates of birth based on current age
def years_ago(years: int) -> date:
    today = date.today()
    try:
        return date(today.year - years, today.month, today.day)
    except ValueError:  # Handle leap year edge case (Feb 29)
        return date(today.year - years, today.month, today.day - 1)

sara = Person(name="Sara", date_of_birth=years_ago(5), children=[])
ahmed = Person(name="Ahmed", date_of_birth=years_ago(8), children=[])

ali = Person(name="Ali", date_of_birth=years_ago(28), children=[sara])
aya = Person(name="Aya", date_of_birth=years_ago(32), children=[ahmed])

imran = Person(name="Imran", date_of_birth=years_ago(55), children=[ali, aya])

def print_family_tree(person: Person) -> None:
    print(f"{person.name} ({person.age()})")
    for child in person.children:
        print(f"  - {child.name} ({child.age()})")
        for grandchild in child.children:
            print(f"    - {grandchild.name} ({grandchild.age()})")

def count_family_members(person: Person) -> int:
    count = 1
    for child in person.children:
        count += count_family_members(child)
    return count

print_family_tree(imran)
print(f"\nTotal family members: {count_family_members(imran)}")
