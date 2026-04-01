# Import date class from the datetime module
from datetime import date
# Import dataclass from dataclasses module 
from dataclasses import dataclass

# Automatically generates a constructor 
@dataclass
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str    
    
    def is_adult(self) -> bool:
        today = date.today()
        date_birth = self.date_of_birth
        age = today.year - date_birth.year - ((today.month, today.day) < (date_birth.month, date_birth.day))
        return age >= 18

imran = Person("Imran", date(1997, 7, 10), "Ubuntu")
print(imran.name)
print(imran.is_adult())

eliza = Person("Eliza", date(1993, 9, 11), "Arch Linux")
print(eliza.name)
print(eliza.is_adult())

