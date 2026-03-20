

class Student:
    def __init__(self):
        self.name = None
        self.age = None
        self.dept = None
        self.cgpa = None

class StudentBuilder:
    def __init__(self):
        self.student = Student()

    def set_name(self, name):
        self.student.name = name
        return self 

    def set_age(self, age):
        self.student.age = age
        return self

    def set_dept(self, dept):
        self.student.dept = dept
        return self 

    def set_cgpa(self, cgpa):
        self.student.cgpa = cgpa
        return self  
    def build(self):
        return self.student

builder = StudentBuilder()
obj = builder.set_name("Asif").set_age(23).set_dept("CSE").set_cgpa(3.43).build()

print(obj.name)