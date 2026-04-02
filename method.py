# This program defines a person with name, birthdate, and favorite OS,
# then checks if the person is an adult (18 or older).

from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()  # Get today's date
        age = today.year - self.date_of_birth.year  # Find age by year difference

        # If birthday hasn't come yet this year, subtract 1 from age
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age >= 18  # Return True if 18 or older

# Create a person named Imran with birthday June 10, 2010
imran = Person("Imran", date(2010, 6, 10), "Ubuntu")
print(imran.is_adult())  # Check if Imran is an adult (True/False)
