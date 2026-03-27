class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address) address is not an attribute of the Person class

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address)


def is_adult(person: Person) -> bool:
    return person.age >= 18


print(is_adult(imran))


# Exercise:
# Write a new function in the file that accepts a Person as a parameter and tries to access a property that
#  doesn’t exist. Run it through mypy and check that it does report an error.


def live_in_london(person: Person) -> bool:
    return person.address == "London"


live_in_london(imran)
