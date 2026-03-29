from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self):
        today = date.today()
        birth_date= self.date_of_birth
        #Calculate exact age by subtracting years
        eighteen_years_ago = date(today.year - 18, today.month, today.day) 
        return birth_date<= eighteen_years_ago  

imran = Person("Imran", date(1989,6,25), "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
print(imran)  # Prints Person(name='Imran', date_of_birth=(1989, 6, 25), preferred_operating_system='Ubuntu')

imran2 = Person("Imran", date(1989,6,25), "Ubuntu")
print(imran == imran2)  # Prints True