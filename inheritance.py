class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        # Call the parent class constructor
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())         # from Parent class
print(person1.get_full_name())    # from Child class

person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())

# The next lines will cause errors, because Parent doesn't have these methods
# print(person2.get_full_name())
# person2.change_last_name("Tyurina")

print(person2.get_name())
# print(person2.get_full_name())


# I learned that Parent and Child classes can have different methods — Parent can’t access methods only defined in Child
# I understood that the child class can add new methods or override existing ones

