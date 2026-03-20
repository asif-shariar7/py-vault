##  In Python, officially there is only one constructor: __init__(), but we use it in different ways:
# 1. Default constructor 2. Parameterized constructor 3. Default value constructor

# 1. Default constructor

class demo: 
    def __init__(self):
         print("Default Constructor Called")

obj = demo()         
    

# 2. Parameterized constructor 

class info:
     def __init__(self, name, age):
          self.name = name
          self.age = age

obj2 = info('Asif', 24)
print(obj2.name, obj2.age)


# 3. default value constructor

class student:
     def __init__(self, name = 'Unknown', age = 0):
          self.name = name
          self.age = age

obj3 = student()   # default value
print(obj3.name, obj3.age)

obj4 = student('Asif', 23)
print(obj4.name, obj4.age)                     

## 3 ta eksathe run korleo object dekhei buzhbe je kon __init__ ta nibe
