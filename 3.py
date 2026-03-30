class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)

#  error: "Person" has no attribute "address" 
#  error: "Person" has no attribute "address" 

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))
# no error


def get_city(person: Person) -> str:
    return person.location
#person has no attribute location.