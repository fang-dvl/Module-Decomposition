from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        dob = self.date_of_birth
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age >= 18


imran = Person(name="Imran", date_of_birth=date(2003, 9, 10), preferred_operating_system="Ubuntu")

print(imran.is_adult())  # Output: True