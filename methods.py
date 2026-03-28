from datetime import date

class Person:
    def __init__(self, name: str, DoB: date, preferred_operating_system: str):
        self.name = name
        self.DoB = DoB
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self)-> bool:
        current_date = date.today()
        age = current_date.year - self.DoB.year - (
            (current_date.month, current_date.day) < (self.DoB.month, self.DoB.day)
        )
        return age >= 18

imran = Person("Imran", date(1998, 1, 6), "Ubuntu")
print(imran.is_adult())