class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str, address: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.address = address

    def is_adult(self) -> bool:
        return self.age >= 18


imran = Person("Imran", 22, "Ubuntu", "123 Main St")
print(imran.name)
print(imran.address)
print(imran.is_adult())

eliza = Person("Eliza", 34, "Arch Linux", "456 Oak Ave")
print(eliza.name)
print(eliza.address)


def get_address(person: Person) -> str:
    return person.address

print(get_address(imran))
