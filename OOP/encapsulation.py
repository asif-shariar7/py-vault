# Encapsulation means wrapping data (variables) and methods (functions) inside a class and  restricting direct access to some details.
# In simple words - Hide internal data and allow access only through methods.

class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.__marks = marks          ## by using __ making private variable. Data is hidden
        # Extra
        self._age = age  

    def get_marks(self):            ## Access is given through a method
        return self.__marks

obj = Student("Asif", 80, 24)
# print(obj.__marks)    -- not accessible. raise errors
print(obj.get_marks())        ##  Accessing private variable through method
print(obj._age)  # this protected variable can accessible            


## Extra - by using _ making protected