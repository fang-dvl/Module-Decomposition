# This program defines a Person with name and age,
# and includes a function to check if they are an adult.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age  # hair_color is NOT defined here

def is_adult(person: Person) -> bool:
    return person.age >= 18  # Returns True if age is 18 or more

# This function will cause an error because 'hair_color' doesn't exist
def print_hair_color(person: Person) -> None:
    print(person.hair_color)  # AttributeError if hair_color not added
