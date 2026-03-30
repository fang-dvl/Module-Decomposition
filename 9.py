class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())
print(person1.get_full_name())
person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
#print(person2.get_full_name())
#person2.change_last_name("Tyurina")
print(person2.get_name())
#print(person2.get_full_name())


#W/O commenting output:
#Elizaveta Alekseeva
#Elizaveta Alekseeva
#Elizaveta Tyurina
#Elizaveta Alekseeva
#Elizaveta Tyurina (née Alekseeva)
#Traceback (most recent call last):
#  File "/Users/Module-Decomposition/prep_exercises/exercise9inheritance.py", line 34, in <module>
#    print(person2.get_full_name())
#AttributeError: 'Parent' object has no attribute 'get_full_name'