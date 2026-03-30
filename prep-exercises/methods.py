from datetime import date

class Person:
    def __init__(self, name: str, DoB: date, preferred_operating_system: str):
        self.name = name
        self.DoB = DoB
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        current_date = date.today()
        age = current_date.year - self.DoB.year - (
            (current_date.month, current_date.day) < (self.DoB.month, self.DoB.day)
        )
        return age >= 18



eliza = Person("Eliza", date(2010, 5, 15), "Arch Linux")
print(f"{eliza.name} is adult: {eliza.is_adult()}")

sara = Person("Sara", date(1995, 12, 20), "macOS")
print(f"{sara.name} is adult: {sara.is_adult()}")
