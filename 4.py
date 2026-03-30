from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

def is_adult(person: Person) -> bool:
    today = date.today()
    dob = person.date_of_birth
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age >= 18

imran_dob = date(2003, 9, 10)
imran = Person("Imran", imran_dob, "Ubuntu")

print(is_adult(imran))  # True