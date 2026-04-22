from datetime import date
class Person:
  def __init__(self, name: str, birthday: date, preferred_operation_system: str):
    self.name = name
    self.birthday = birthday
    self.preferred_operation_system = preferred_operation_system
  
  def is_adult(self) -> bool:
    today = date.today()
    years = today.year - self.birthday.year
    if (today.month, today.day) < (self.birthday.month, self.birthday.day):
      years -= 1 
    return years >= 18

imran = Person("Imran", date(2000, 10, 12) , "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", date(1992, 5, 17), "Arch linux")
print(eliza.name)
print(eliza.address)

def is_adult(person: Person) -> bool:
  return person.age >= 18

print(is_adult(imran))

def print_address(person: Person) -> None:
  print(person.address)
  