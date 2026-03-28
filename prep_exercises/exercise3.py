'''Exercise
Save the above code to a file, and run it through mypy.

Read the error, and make sure you understand what it’s telling you.
'''
from typing import Optional

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str) -> None:
        self.name: str = name
        self.age: int = age
        self.preferred_operating_system: str = preferred_operating_system
        # Optional attribute; not set by default
        self.address: Optional[str] = None  

# Create instances
imran = Person("Imran", 22, "Ubuntu")
eliza = Person("Eliza", 34, "Arch Linux")

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))  # True
print(is_adult(eliza))  # True

def print_address(person: Person) -> None:
    if person.address is None:
        print(f"{person.name} has no address set.")
    else:
        print(person.address)

