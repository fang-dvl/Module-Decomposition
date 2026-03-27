import sys
from enum import Enum
from dataclasses import dataclass

class OperatingSystem(Enum):
  MACOS = "macOS"
  ARCH = "Arch Linux"
  UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Laptop:
  id: int
  manufacturer: str
  model: str
  screen_size_in_inches: float
  operating_system: OperatingSystem

laptops = [
  Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
  Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
  Laptop(id=3, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
  Laptop(id=4, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=15, operating_system=OperatingSystem.MACOS),
]

# user input
try:
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  os_input = input("Enter your preferred operating system (macOS / Arch Linux / Ubuntu): ")

  # Convert string to enum
  preferred_os = OperatingSystem(os_input)
except ValueError:
  print("Invalid input. Please check your age or operating system name.", file=sys.stderr)
  sys.exit(1)

# count available laptops
matching_laptops = [l for l in laptops if l.operating_system == preferred_os]
print(f"{name}, there are {len(matching_laptops)} laptops available with {preferred_os.value}.")

# suggest alternative OS if another has more laptops
os_counts = {
  os: sum(1 for l in laptops if l.operating_system == os) 
  for os in OperatingSystem
}

most_common_os = max(os_counts, key=lambda os: os_counts[os])

if most_common_os != preferred_os:
  print(f"If you can use {most_common_os.value}, you have a higher chance of getting a laptop.")


# I learned how to use Enums to make my code safer and avoid typos.
# I also learned how to handle invalid user input safely using try and except.
# Using lambda helps mypy understand the type more clearly.
# Without it, mypy didn't know what os_counts.get returns.
