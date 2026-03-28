'''
Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

Re-add the is_adult method to it.'''

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day): #if bd havent occured even once this year -1
            age -= 1
        return age >= 18

#example
imran = Person("Imran", date(2003, 7, 14), "Ubuntu")
eliza = Person("Eliza", date(1991, 3, 25), "Arch Linux")
print(imran)
print(imran.is_adult())
print(eliza.is_adult())