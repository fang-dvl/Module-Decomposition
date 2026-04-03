from datetime import date

class Person:
    def __init__(self, name: str, dob: date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system


    def is_adult (self) -> bool:
        today = date.today()
        age = today.year - self.dob.year - ((today.month,today.day)<(self.dob.month,self.dob.day))
        return age >=18

person1 = Person("AYK",date(1990,8,15),"mac")

print (person1.name + " born on " + str(person1.dob)+ " and like " + person1.preferred_operating_system)
print(person1.is_adult())