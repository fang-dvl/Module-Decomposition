from datetime import date


class Person:
    # a constructor with a new instance of class
    def __init__(self, name: str, date_of_birth:date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        today_date = date.today()
        birth_date= self.date_of_birth
        #to check date and month as well
        age = today_date.year-birth_date.year- ((today_date.month, today_date.day) < (birth_date.month, birth_date.day)) 
        return age>=18


imran = Person("Imran", date(1989,6,25), "Ubuntu")
print(imran.name)
print(imran.is_adult())

eliza = Person("Eliza", date(2007,10,12), "Arch Linux")
print(eliza.is_adult())



