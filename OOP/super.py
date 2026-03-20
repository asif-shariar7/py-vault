# super() Lets you call parent methods without directly naming the parent
## super() lets a child class reuse and extend parent functionality while respecting Python’s inheritance hierarchy (MRO - Method Resolution Order)


class Student:
    def __init__(self, name):
        self.name = name
        print("Parent Constructor")

class Course(Student):
    def __init__(self, title, name):
        super().__init__(name)   # call parent (Student) constructor using super()
        self.title = title
        print("Child Constructor")

obj = Student('Asif')
obj2 = Course('Data Science','Asif')

print(obj2.name)    # output - 
                            # Parent Constructor
                            # Parent Constructor
                            # Child Constructor
                            # Asif    

## for call parent method

class Demo:
    def show(self):
        print("Show Parent")

class Dummy(Demo):
    def show(self):
        super().show()    # call parent method
        print("Show Child")

ob = Dummy()
ob.show()