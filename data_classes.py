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

# Example usage
imran = Person("Imran", date(2001, 5, 15), "Ubuntu")
print(imran)  # Prints Person(name='Imran', date_of_birth=datetime.date(2001, 5, 15), preferred_operating_system='Ubuntu')
print(imran.is_adult())  # Prints True or False depending on the current date