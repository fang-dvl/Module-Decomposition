from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
        return age >= 18

imran = Person(name="Imran", date_of_birth=date(2003, 7, 14), preferred_operating_system="Ubuntu")
print(imran)                
print(imran.is_adult())     

# Equality check
imran2 = Person(name="Imran", date_of_birth=date(2003, 7, 14), preferred_operating_system="Ubuntu")
print(imran == imran2)   