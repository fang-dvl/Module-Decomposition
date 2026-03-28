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
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
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
    print(f"Age must be a number")
    exit()

preferred_os_input = input('Please enter your preferred operating system: ')
try:
    preferred_operating_system = OperatingSystem(preferred_os_input)
except ValueError:
    print(f'We are not offering {preferred_os_input}. Please choose from the following list: {[os.value for os in OperatingSystem]}')
    exit()



person = Person(name=name, age=age, preferred_operating_system=preferred_operating_system)


number_of_available_laptops = sum(
    1 for laptop in laptops if laptop.operating_system == person.preferred_operating_system
)

def offer_laptop_to_user()->None:
    offer = input('Would you like a laptop with this OS (yes / no) ? ')
    if offer.lower() == "y" or offer.lower() == "yes":
        print(f'Great! Please come on monday next week to collect your laptop')
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


