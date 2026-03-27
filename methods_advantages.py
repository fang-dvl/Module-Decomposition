class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        return self.age >= 18


imran = Person("Imran", 22, "Ubuntu")

print(imran.is_adult())  # True

# Advantages of using methods instead of free functions:
# 1. Easier documentation - all related behaviors are attached to the class.
# 2. Encapsulation - data and logic are kept together in one place.
# 3. Easier maintenance - when class details change, methods can be updated easily.
# 4. Clearer code - you can write person.is_adult() instead of is_adult(person).