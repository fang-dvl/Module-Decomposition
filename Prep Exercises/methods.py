from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def is_adult(self) -> bool:
        return self.age >= 18

imran = Person(
    name="Imran",
    date_of_birth=date(2003, 7, 14),
    preferred_operating_system="Ubuntu"
)

print(f"{imran.name} is {imran.age} years old.")
print(f"Is {imran.name} an adult? {imran.is_adult()}")
