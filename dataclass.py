from datetime import date
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        eighteen_birthday = date(
            self.date_of_birth.year + 18,
            self.date_of_birth.month,
            self.date_of_birth.day,
        )
        return date.today() >= eighteen_birthday


imran = Person("Imran", date(2019, 12, 22), "Ubuntu")
print(imran.is_adult())

imran2 = Person("Imran2", date(2000, 12, 22), "Ubuntu")
print(imran2.is_adult())

print(imran == imran2)
