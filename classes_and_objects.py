class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
            return self.age >= 18

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address) # address is not an attribute of the Person class
print(imran.is_adult())

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address)# address is not an attribute of the Person class

def get_address(person: Person) -> str:
     return person.address

print(get_address(imran))