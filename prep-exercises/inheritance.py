class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: list[str] = []

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


print("Creating Child instance:")
person1 = Child("Sarah", "Johnson")
print(f"Name: {person1.get_name()}")
print(f"Full name: {person1.get_full_name()}")

print("\nChanging last name to Smith:")
person1.change_last_name("Smith")
print(f"Name: {person1.get_name()}")
print(f"Full name: {person1.get_full_name()}")

print("\nCreating Parent instance:")
person2 = Parent("Emma", "Wilson")
print(f"Name: {person2.get_name()}")

# person2.change_last_name("Brown")  # Error: Parent doesn't have change_last_name method
