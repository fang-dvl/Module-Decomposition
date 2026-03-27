from datetime import date

class Person:
  def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
    self.name = name
    self.date_of_birth = date_of_birth
    self.preferred_operating_system = preferred_operating_system

  def is_adult(self) -> bool:
    today = date.today()
    age = today.year - self.date_of_birth.year - (
      (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
      )
    return age >= 18


imran = Person("Imran", date(2002, 5, 15), "Ubuntu")
print(imran.is_adult())  # True

# I learned that methods can easily adapt to changes inside a class.
# Now the class stores a date of birth instead of age, but the method still works correctly.
