# This program creates a person with children and prints a simple family tree.

from dataclasses import dataclass
from typing import List

# Define a Person with a name, age, and a list of children (who are also Person objects)
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: List["Person"]  # List of other Person objects

# Create children
fatma = Person(name="Fatma", age=5, children=[])
aisha = Person(name="Aisha", age=7, children=[])

# Create parent with children
imran = Person(name="Imran", age=35, children=[fatma, aisha])

# Print person's name and their children
def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")  # Print each child's name and age

print_family_tree(imran)  # Show family tree starting from Imran
