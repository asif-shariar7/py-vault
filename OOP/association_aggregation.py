# Passing an object from one class to another = association
# Association means: One class is connected to another class (they work together)


class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj  # association (uses) / aggregation (has a) ???

    def show(self):
        print(f"My name is {self.name}. I use a laptop named {self.laptop_v.brand}")    


obj = Laptop("Walton")
obj2 = Student("Asif", obj)
obj2.show()


# 1. Is Student just using Laptop?
# ✔ Yes → Association

# 2. Does Student “have a” Laptop?
# ✔ Yes → Aggregation

# Note:
# Aggregation is a type of association
# So: All aggregation = association . But not all association = aggregation 
# Objects are independent for both