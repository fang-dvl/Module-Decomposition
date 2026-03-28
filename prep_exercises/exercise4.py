'''
Think of the advantages of using methods instead of free functions. Write them down in your notebook.
Ease of documentation - it makes it easier to find all of the things related to a string (or a Person) if they’re attached to that type.
Encapsulation - if we change the implementation of Person (e.g. we start storing a date of birth instead of an age), it’s more obvious what things we need to change.
'''
'''
Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.

Update the is_adult method to act the same as before.'''

from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str) -> None:
        self.name: str = name
        self.date_of_birth: date = date_of_birth
        self.preferred_operating_system: str = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        # Calculate age in years
        age = today.year - self.date_of_birth.year
        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18

# Example usage
imran = Person("Imran", date(2001, 3, 15), "Ubuntu")
print(imran.is_adult())  # True if 18 or older
