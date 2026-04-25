from datetime import date
class Person:
  def __init__(self, name: str, age: int, preferred_operation_system: str):
    self.name = name
    self.age = age
    self.preferred_operation_system = preferred_operation_system
  
  def is_adult(self) -> bool:
    return self.age >= 18

imran = Person("Imran", 22 , "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch linux")
print(eliza.name)
print(eliza.address)

def is_adult(person: Person) -> bool:
  return person.age >= 18

print(is_adult(imran))

def print_address(person: Person) -> None:
  print(person.address)


# mypy prints: error: "Person" has no attribute "address"  [attr-defined]. We try to access
# a not defined field of the Person class.