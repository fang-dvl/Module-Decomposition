from dataclasses import dataclass
from enum import Enum
import sys
from collections import Counter


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


users = []


def find_possible_laptops(laptops: list[Laptop], person: Person) -> list[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


def input_validation() -> tuple[str, int, OperatingSystem]:
    input_user_name = input("Enter your name: ")
    if not isinstance(input_user_name, str):
        sys.stderr.write("Name must be a string")
        sys.exit(1)

    try:
        input_user_age = int(input("Enter your age: "))
    except ValueError:
        sys.stderr.write("Age must be an integer")
        sys.exit(1)

    input_preferred_operating_system = input(
        "Enter your preferred operating system (macOS/Arch Linux/Ubuntu): "
    )

    try:
        preferred_os = OperatingSystem(input_preferred_operating_system)
    except ValueError:
        sys.stderr.write("Wrong OS")
        sys.exit(1)

    return input_user_name, input_user_age, preferred_os


def count_operating_systems(laptops: list[Laptop]) -> Counter[OperatingSystem]:
    return Counter(laptop.operating_system for laptop in laptops)


def recommend_os(user: Person, laptops: list[Laptop]) -> None:
    os_counts = count_operating_systems(laptops)
    most_common_os, most_common_count = os_counts.most_common(1)[0]

    user_preferred_os = os_counts[user.preferred_operating_system]

    if (
        most_common_os != user.preferred_operating_system
        and user_preferred_os < most_common_count
    ):
        print(f"More laptops are available with {most_common_os.value}.")


def laptop() -> None:
    input_user_name, input_user_age, input_preferred_operating_system = (
        input_validation()
    )

    users.append(
        Person(
            name=input_user_name,
            age=input_user_age,
            preferred_operating_system=OperatingSystem(
                input_preferred_operating_system
            ),
        ),
    )
    for user in users:
        possible_laptops = find_possible_laptops(laptops, user)
        print(
            f"Possible laptops for {user.name}:\n{'\n'.join(map(str, possible_laptops))}",
        )
        recommend_os(user, laptops)


laptop()
