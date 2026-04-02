# This code defines a Person with a name, date of birth, and favorite operating system.
# It also checks if the person is 18 years old or older.

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)  # Makes the object read-only after creation
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()  # Get today's date
        age = today.year - self.date_of_birth.year  # Calculate age
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1  # Subtract 1 if birthday hasn't happened yet this year
        return age >= 18  # True if age is 18 or more

imran = Person("Imran", date(2010, 6, 10), "Ubuntu")  # Create a person
print(imran)  # Show person info
print(imran.is_adult())  # Check if Imran is an adult