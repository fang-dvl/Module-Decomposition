class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


imran = Person("Imran", 22, "Ubuntu")
eliza = Person("Eliza", 34, "Arch Linux")

print(imran.name)
# print(imran.address)  # mypy error: Person has no attribute "address"

print(eliza.name)
# print(eliza.address)  # mypy error again

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))  # no mypy error

def print_address(person: Person) -> None:
    print(person.address)  # mypy will catch this too

# I learned that a class defines what attributes each object will have.
# Mypy can check if I try to access an attribute that doesn't exist.
# It helps to avoid mistakes like typing person.addres instead of person.address.
