# class vs instance variable

class Student:
    college_name = 'ABC' # class variable (shared/common/same for all objects)

    def __init__(self, name):
        self.name = name   # instance variable (unique for every object)


obj = Student('Asif')
obj2 = Student('Shariar')


print(obj.name)   # Asif
print(obj2.name)    # Shariar

print(obj.college_name) # ABC
print(obj2.college_name) # ABC