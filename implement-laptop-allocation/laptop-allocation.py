from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class OperatingSystem(Enum):
  MACOS = "MacOS"
  ARCH = "Arch Linux"
  UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
  name: str
  age: int
  # sorted in order of preference, most preferred is first
  preferred_operating_systems: tuple

@dataclass(frozen=True)
class Laptop:
  id: int
  manufacturer: str
  model: str
  screen_size_in_inches: float
  operating_system: OperatingSystem


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
  result: Dict[Person, Laptop] = {}
  available_laptops = laptops.copy()
  
  for person in people:
    laptop_found = False
    for i in range(len(person.preferred_operating_systems)):
      for laptop in available_laptops:
        if (person.preferred_operating_systems[i] == laptop.operating_system):
          laptop_found = True
          result[person] = laptop
          available_laptops.remove(laptop)
          break

      if laptop_found:
        break

  for person in people:
    if not len(available_laptops):
      break
    if not person in result.keys():
      result[person] = available_laptops.pop()

  return result

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

people = [
  Person("Imran", 22, (OperatingSystem.ARCH,)),
  Person("Eliza", 34, (OperatingSystem.MACOS, OperatingSystem.UBUNTU))
]

allocated = allocate_laptops(people, laptops)

for person in allocated.keys():
  print(person.name, allocated[person].id)
