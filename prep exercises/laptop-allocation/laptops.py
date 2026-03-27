from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from typing import Dict, List, Tuple

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
    WINDOWS = "windows"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: Tuple[OperatingSystem, ...]

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "preferred_operating_systems",
            tuple(self.preferred_operating_systems),
        )

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def sadness_for_allocation(person: Person, laptop: Laptop) -> int:
    try:
        return person.preferred_operating_systems.index(laptop.operating_system)
    except ValueError:
        return 100


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    if len(laptops) < len(people):
        raise ValueError("Not enough laptops to allocate exactly one per person")

    people_tuple: Tuple[Person, ...] = tuple(people)
    laptops_tuple: Tuple[Laptop, ...] = tuple(laptops)

    @lru_cache(maxsize=None)
    def best_from(person_index: int, used_mask: int) -> Tuple[int, Tuple[int, ...]]:
        if person_index == len(people_tuple):
            return 0, tuple()

        best_total_sadness = float("inf")
        best_choice: Tuple[int, ...] = tuple()

        for laptop_index, laptop in enumerate(laptops_tuple):
            if used_mask & (1 << laptop_index):
                continue

            current_sadness = sadness_for_allocation(people_tuple[person_index], laptop)
            remaining_sadness, remaining_choices = best_from(
                person_index + 1,
                used_mask | (1 << laptop_index),
            )
            candidate_total = current_sadness + remaining_sadness

            if candidate_total < best_total_sadness:
                best_total_sadness = candidate_total
                best_choice = (laptop_index,) + remaining_choices

        return best_total_sadness, best_choice

    _, selected_laptop_indexes = best_from(0, 0)

    return {
        person: laptops_tuple[laptop_index]
        for person, laptop_index in zip(people_tuple, selected_laptop_indexes)
    }