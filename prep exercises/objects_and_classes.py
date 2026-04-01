from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: str, preferred_operating_system: str, address: str):
        self.name = name
        self.date_of_birth = date.fromisoformat(date_of_birth)
        self.preferred_operating_system = preferred_operating_system
        self.address = address

    def is_adult(self):
        today_date = date.today()

        return (today_date.year - self.date_of_birth.year) >= 18


imran = Person("Imran", "2005-12-04", "Ubunut", "Wardend Road, Birmingham")

print(imran.is_adult())