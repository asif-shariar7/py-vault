## ----

# class Singleton:
#     _instance = None     # class variable to store single object

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)   # create object once
#         return cls._instance
            

# # Testing
# obj1 = Singleton()
# obj2 = Singleton()

# print(obj1 is obj2)   # True (same object)

##########
## How it works  --->
# __new__() controls object creation
# First time:
# _instance is None → object is created
# Next times:
# Existing object is returned
##########

### 

class Singleton:
    _instance = None     # class variable to store single object

    def __new__(cls):
        if cls._instance is None:
            print("Hello")
            cls._instance = super().__new__(cls)   # create object once
        return cls._instance
            

# Testing
obj1 = Singleton()
obj2 = Singleton()

# Output - Hello (Here only one time created)
