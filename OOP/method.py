## Instance method (self) → works with object data. self.variable → belongs to object
# Class method (cls) → works with class data. cls.variable → belongs to class

class Student:
    college = "ABC"   # class variable

    def __init__(self, name, college):
        self.name = name    # instance variable
        self.college_name = college

    def show_name(self):     # instance method
        print(self.name)  


    @classmethod      # called decorator - classmethod use for class method declaration
    def show_college(cls):   # class method
        print(cls.college)


obj = Student('Asif', 'XYZ')
print(obj.college_name)  # XYZ
obj.show_name()    # instance method - Asif
Student.show_college() # class method - ABC
