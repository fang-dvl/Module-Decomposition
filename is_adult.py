from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        eighteen_birthday = date(
            self.date_of_birth.year + 18,
            self.date_of_birth.month,
            self.date_of_birth.day,
        )
        return date.today() >= eighteen_birthday


imran = Person("Imran", date(2019, 12, 22), "Ubuntu")
print(imran.is_adult())
