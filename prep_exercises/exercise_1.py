class Parent:                                                   # declares class Parent
    def __init__(self, first_name: str, last_name: str):        # declares constructor with first_name, last_name string parameters
        self.first_name = first_name                            # assign first_name argument value to the field
        self.last_name = last_name                              # assign last_name argument value to the field

    def get_name(self) -> str:                                  # declares get_name method, returns string
        return f"{self.first_name} {self.last_name}"            # concatenate and return first_name last_name fields values


class Child(Parent):                                            # declares Child class inheriting Parent class
    def __init__(self, first_name: str, last_name: str):        # declares constructor with first_name, last_name string parameters
        super().__init__(first_name, last_name)                 # calls parent class constructor
        self.previous_last_names = []                           # assign empty array to previous_last_names field

    def change_last_name(self, last_name) -> None:              # declares change_last_name method with last name parameter
        self.previous_last_names.append(self.last_name)         # add the current value of the last_name field to the previous_last_name list end
        self.last_name = last_name                              # assign the las name argument value to last_name field

    def get_full_name(self) -> str:                             # declares get_full_name method returns string
        suffix = ""                                             # declares variable suffix and assigns empty string to it
        if len(self.previous_last_names) > 0:                   # checks is not the previous_last_names list empty
            suffix = f" (née {self.previous_last_names[0]})"    # if list is not empty concatenate strings "(née " "first_element_of_list" ")" and assigns to suffix variable
        return f"{self.first_name} {self.last_name}{suffix}"    # concatenates and returns first_name last_name fields and suffix variable values

person1 = Child("Elizaveta", "Alekseeva")                       # creates Child class object and assign to person1 variable
print(person1.get_name())                                       # prints get_name method of person1 call result: 'Elizaveta Alekseeva'
print(person1.get_full_name())                                  # prints get_full_name method of person1 call result: 'Elizaveta Alekseeva'
person1.change_last_name("Tyurina")                             # call change_last_name method of the person1 object with argument "Tyurina"
print(person1.get_name())                                       # print get_name method of person1 call result: 'Elizaveta Tyurina'
print(person1.get_full_name())                                  # prints get_full_name method of person1 call result: 'Elizaveta Tyurina (née Alekseeva)'

person2 = Parent("Elizaveta", "Alekseeva")                      # creates Person class object and assign to person2 variable
print(person2.get_name())                                       # prints get_name method of person1 call result: 'Elizaveta Alekseeva'
print(person2.get_full_name())                                  # prints get_full_name method what will invoke an error cause Person class doesn't have such method
person2.change_last_name("Tyurina")                             # call change_last_name method of the person2 object with argument "Tyurina" what will invoke an error cause Person class doesn't have such method
print(person2.get_name())                                       # prints get_name method of person1 call result: 'Elizaveta Alekseeva'
print(person2.get_full_name())                                  # prints get_full_name method what will invoke an error cause Person class doesn't have such method  