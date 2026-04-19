from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
  name: str
  birthday: date
  preferred_operation_system: str

imran = Person("Imran", date(2000, 10, 25), "Ubuntu")

imran2 = Person("Imran", date(2000, 10, 25), "Ubuntu")

print(imran)

print(imran == imran2)
