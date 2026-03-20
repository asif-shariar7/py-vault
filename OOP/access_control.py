## implemented encapsulation using private variables + getter/setter.
# Private = “don’t touch directly, use methods instead”

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.__salary = salary

    def get_salary(self, password):
        if password == 'admin':
            print(self.__salary)
        else:
            print("Invalid access!!")

    def set_salary (self, password, salary):
        if password == 'admin':
            self.__salary = salary
            print(f"New salary: {self.__salary}")
        else:
            print("Invalid access!!")


obj = Employee('Asif',30000)
print(obj.name)   # Asif
print(obj.__salary)   ## Error arise
obj.get_salary("ad")   # invalid access!!
obj.get_salary("admin")  # prints salary
obj.set_salary("admin", 70000)  # updates salary for correct password


## Note:
# Using plain "admin" password like this is not real security. 
# This is just for learning encapsulation, not real authentication.
