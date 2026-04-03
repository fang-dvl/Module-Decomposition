from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    name: str
    dob: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.dob.year - ((today.month,today.day)<(self.dob.month,self.dob.day))
        return age >= 18

# Example usage
person1 = Person(name="AYK", dob=date(1989, 7, 15), preferred_operating_system="mac")

print(person1.name)  # AYK
print(person1.is_adult())