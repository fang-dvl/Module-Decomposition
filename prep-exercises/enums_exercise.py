from dataclasses import dataclass
from enum import Enum

class OperatingSystem(Enum):
    MACOS = "macOS"
    UBUNTU = "Ubuntu"
    ARCH = "Arch Linux"

@dataclass
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

laptops = [
    Laptop(id=1, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="HP", model="Pavilion", screen_size_in_inches=15.6, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Asus", model="ZenBook", screen_size_in_inches=13.3, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

@dataclass
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


name = input('Please enter your name: ')

age_input = input('Please enter your age: ')
try:
    age = int(age_input)
except ValueError:
    print(f"Error: '{age_input}' is not a valid age. Please enter a number.")
    exit()

preferred_os_input = input('Please enter your preferred operating system: ')
try:
    preferred_operating_system = OperatingSystem(preferred_os_input)
except ValueError:
    available_options = ', '.join([os.value for os in OperatingSystem])
    print(f"Error: '{preferred_os_input}' is not available. Please choose from: {available_options}")
    exit()


person = Person(name=name, age=age, preferred_operating_system=preferred_operating_system)


number_of_available_laptops = sum(
    1 for laptop in laptops if laptop.operating_system == person.preferred_operating_system
)

def offer_laptop_to_user() -> None:
    offer = input('Would you like a laptop with this OS (yes / no) ? ')
    if offer.lower() == "y" or offer.lower() == "yes":
        print('Great! Please come on monday next week to collect your laptop')
    else:
        print('No problem. See you later.')

if number_of_available_laptops == 1:
    print(f'There is {number_of_available_laptops} laptop available with your preferred operating system.')
    offer_laptop_to_user()
elif number_of_available_laptops > 1:
    print(f'There are {number_of_available_laptops} laptops available with your preferred operating system.')
    offer_laptop_to_user()
else:
    print('There are no laptops available with your preferred operating system.')
