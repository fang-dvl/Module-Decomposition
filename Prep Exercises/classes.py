class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

def is_adult(person: Person) -> bool:
    return person.age >= 18

def location(person: Person) -> str:
    return person.location 

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address) # Person has no address attribute
print(imran.age)
print(is_adult(imran))
print(location(imran))

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address) # Person has no address attribute
print(eliza.age)
print(is_adult(eliza))