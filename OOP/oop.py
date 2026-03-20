## OOP use for organizations mainly

class className: 
    salary = 15000              ## must use self always
    def funName (self, name):
        print(f"Hello! I am {name}. I have {self.salary} TK")

obj = className()

obj.funName("Asif")



class demo:
    pass        # pass statement


## Default Constructor

class Person:
    def __init__(self):
        print("Hello")

obj = Person()   ##prints the Hello



##Parameterized Constructor

class personDemo:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show (self):
        print(f"Hello! I am {self.name}. My salary is {self.salary}")

obj = personDemo("Asif",170000)    # here constructor call happens
obj.show() 