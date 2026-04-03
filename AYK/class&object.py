class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)


def is_adult (person: Person) ->bool:
    return person.age >=18

print(is_adult(imran))

def current_address (address : Person):
    return address.location;

