from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
  name: str
  age: int
  children: List["Person"]

fatima = Person("Fatima", 6, [])
aisha = Person("Aisha", 3, [])

imran = Person("Imran", 32, [fatima, aisha])

def print_family_tree(person: Person) -> None:
  print(person.name)
  for child in person.children:
    print(f"{child.name} ({child.age})")

print_family_tree(imran)
