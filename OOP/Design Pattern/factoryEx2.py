
class Car:
    def __init__(self,name, brand):
        self.name = name
        self.brand = brand

    def show(self):
        print(f"Car name : {self.name} and brand : {self.brand}")  


class Bike:
    def __init__(self,name, brand):
        self.name = name
        self.brand = brand

    def show(self):
        print(f"Bike name : {self.name} and brand : {self.brand}") 


class VehicleFactory:
    def check_vehicle (self, vehicle_type, name, brand):
        vehicle = {
            "car" : Car,
            "bike" : Bike
        }

        if vehicle_type not in vehicle:
            raise ValueError ("Invalid!!")
        return vehicle[vehicle_type](name, brand)
    

factory = VehicleFactory() 

v1 = factory.check_vehicle("car", "Toyota", "V8")
v1.show()