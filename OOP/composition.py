# Composition is a stronger type of “has-a” relationship than aggregation.

class Engine:
    def __init__(self, type):
        self.type = type

class Car:
    def __init__(self, name, engine_type):
        self.name = name
        self.engine = Engine(engine_type)   ## composition: Car owns Engine

    def show(self):
        print(f"{self.name} has an engine of type {self.engine.type}")    


obj = Car("Toyota", "V8")
obj.show()    



## Why this is composition ->
# Engine is created inside Car
# It does not exist independently
# If Car object is destroyed → its Engine is destroyed too

## Note:

# Association → uses
# Aggregation → has-a (independent)
# Composition → has-a (dependent)