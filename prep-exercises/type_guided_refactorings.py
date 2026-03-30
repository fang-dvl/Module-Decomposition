from dataclasses import dataclass
from typing import Optional

# Before refactoring - unclear types
def process_user_data(data):
    name = data[0]
    age = data[1]
    email = data[2] if len(data) > 2 else None
    
    if age < 18:
        return None
    
    return f"{name} ({age}): {email or 'no email'}"


# After refactoring - clear types
@dataclass
class User:
    name: str
    age: int
    email: Optional[str] = None

def is_adult(user: User) -> bool:
    return user.age >= 18

def format_user_info(user: User) -> str:
    email_str = user.email if user.email else "no email"
    return f"{user.name} ({user.age}): {email_str}"

def process_user(user: User) -> Optional[str]:
    if not is_adult(user):
        return None
    return format_user_info(user)


# Testing old version
print(process_user_data(("Alice", 25, "alice@example.com")))
print(process_user_data(("Bob", 16)))

# Testing new version
user1 = User("Alice", 25, "alice@example.com")
user2 = User("Bob", 16)

print(process_user(user1))
print(process_user(user2))


# Another example
def get_value(key: str, data: dict[str, int]) -> Optional[int]:
    return data.get(key)

sample_data = {"a": 1, "b": 2}
result = get_value("a", sample_data)
if result is not None:
    print(f"Found: {result}")
