# staticmethod - A method that belongs to a class but does not access the instance (self) or the class (cls). 
# Static methods let you call a method without creating an object.You don’t need self because it doesn’t depend on instance data.


class Student:

    @staticmethod
    def add(a,b):
        return a+b
    

# Call without creating an object -
print(Student.add(3,4))


# Call using object (also works)
obj = Student()
print(obj.add(4,6))