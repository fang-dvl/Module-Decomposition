from enum import Enum
import sys

# Define the possible operating systems as an enum
class OperatingSystem(Enum):
    MACOS = "MacOS"
    ARCH = "Arch"
    UBUNTU = "Ubuntu"

# List of laptops available in the library
laptops = [
    {"id": 1, "manufacturer": "Dell", "model": "XPS", "os": OperatingSystem.ARCH},
    {"id": 2, "manufacturer": "Dell", "model": "XPS", "os": OperatingSystem.UBUNTU},
    {"id": 3, "manufacturer": "Dell", "model": "XPS", "os": OperatingSystem.UBUNTU},
    {"id": 4, "manufacturer": "Apple", "model": "MacBook", "os": OperatingSystem.MACOS},
    {"id": 5, "manufacturer": "Dell", "model": "Inspiron", "os": OperatingSystem.UBUNTU},
]

def get_user_preferences():
    """Get the user's name and preferred operating system"""
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be empty", file=sys.stderr)
        sys.exit(1)
    
    print("\nAvailable operating systems:")
    print("• MacOS")
    print("• Arch") 
    print("• Ubuntu")
    
    os_choice = input("Enter your preferred operating system: ").strip().lower()
    
    # Convert string to OperatingSystem enum
    if os_choice == "macos":
        return name, OperatingSystem.MACOS
    elif os_choice == "arch":
        return name, OperatingSystem.ARCH
    elif os_choice == "ubuntu":
        return name, OperatingSystem.UBUNTU
    else:
        print(f"Error: '{os_choice}' is not a valid operating system", file=sys.stderr)
        print("Please choose from: macos, arch, ubuntu", file=sys.stderr)
        sys.exit(1)

def count_laptops_by_os():
    """Count how many laptops we have for each operating system"""
    counts = {}
    for os in OperatingSystem:
        counts[os] = 0
    
    for laptop in laptops:
        counts[laptop["os"]] += 1
    
    return counts

def main():
    print("=== Library Laptop Finder ===")
    
    # Get user input
    name, preferred_os = get_user_preferences()
    
    # Count laptops for each OS
    os_counts = count_laptops_by_os()
    
    # Show results to user
    user_laptop_count = os_counts[preferred_os]
    
    print(f"\nHello {name}!")
    print(f"We have {user_laptop_count} laptop(s) with {preferred_os.value}.")
    
    # Check if other OS have more laptops
    other_options = []
    for os, count in os_counts.items():
        if os != preferred_os and count > user_laptop_count:
            other_options.append((os, count))
    
    if other_options:
        print("\nTip: These operating systems have more laptops available:")
        for os, count in other_options:
            print(f"  • {os.value}: {count} laptops")
    
    # Show complete availability
    print(f"\nAll available laptops:")
    for os in OperatingSystem:
        count = os_counts[os]
        print(f"  • {os.value}: {count} laptop(s)")

if __name__ == "__main__":
    main()