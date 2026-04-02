# This program shows inheritance: a Child class that extends Parent and adds extra features.

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)  # Use Parent's init
        self.previous_last_names = []  # Track old last names

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


# Create a Child object and test name changes
person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())         # Elizaveta Alekseeva
print(person1.get_full_name())    # Elizaveta Alekseeva
person1.change_last_name("Tyurina")
print(person1.get_name())         # Elizaveta Tyurina
print(person1.get_full_name())    # Elizaveta Tyurina (née Alekseeva)

# Create a Parent object
person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())         # Works: method exists

# The following lines will cause errors because Parent doesn't have those methods
# print(person2.get_full_name())  # Error: Parent has no get_full_name()
# person2.change_last_name("Tyurina")  # Error: Parent has no change_last_name()
# print(person2.get_full_name())  # Error again

# To fix the errors above, you'd need to check the object type before calling those methods
