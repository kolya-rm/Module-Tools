from dataclasses import dataclass
from enum import Enum
from typing import List

class OperatingSystem(Enum):
  MACOS = "MacOS"
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
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

name = input("Input name: ")
age = int(input("Input age: "))
os = OperatingSystem(input("Input operating system: "))

person = Person(name, age, os)

count = 0
for laptop in laptops:
  if person.preferred_operating_system == laptop.operating_system:
    count += 1
  
print(f"Available {count} laptops with {person.preferred_operating_system}")