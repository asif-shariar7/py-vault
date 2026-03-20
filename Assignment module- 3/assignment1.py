## Create a class named Car with the attributes brand, model, and year. Include a constructor to initialize these values and a method display_info() to print all the car details. Then create an object of the Car class and display its details.



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nYear : {self.year}")

obj = Car("Tesla", "Model 3", 2022)
obj.display_info()