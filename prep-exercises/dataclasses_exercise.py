from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        current_date = date.today()
        age = current_date.year - self.date_of_birth.year - (
            (current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
        return age >= 18

# Example usage:
imran = Person("Imran", date(2001, 5, 15), "Ubuntu")
print(imran)
print(imran.is_adult())

eliza = Person("Eliza", date(1990, 3, 20), "Arch Linux")
print(eliza)
print(eliza.is_adult())

