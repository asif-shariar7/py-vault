## 

# def function_name ():
#     print("Hello")

# function_name()    


## function with parameter

def function_name (fname):
    print("Hello", fname)

def funcName (fname, lname):
    print(fname + " " + lname) 

function_name("Asif")    # this is argument
funcName("Asif", "Shariar")

## keyword argument. pass argument using parameter names

def keyword_func (name, age):
    print(f"Hello I am {name}. I am {age} years old!")

keyword_func(name = "Asif", age = 24)   ## order doesn't matter


## with default parameter value

def default_func (name = "Asif"):
    print("Hello", name)

default_func()     ## without argument it choose the default value
default_func("Shariar")  


## return statement

def add (a , b):
    return (a+b)

print(add(3,4))

## loop in function
def loop_func (food):
    for i in food:
        print(i)

fruits = ["apple", "banana", "mango"]
loop_func(fruits)   


## pass statement

def pass_func ():
    pass              # do nothings just pass

## if the function doesn't know how many argument will pass - arbitrary parameter then use *any_name

def funame (*name):
    print("Hello", name)  # Hello ('Asif','Shariar')
    print(name[1])     #Shariar. because indexing happens

funame("Asif", "Shariar")  

## if the function doesn't know how many keyword argument will pass then use **any_name as parameter (arbitrary keyword argument)


def key_func(**arg):
    print(arg)     #{'name': 'Asif', 'age': 24}
    print (arg["name"])    # access by this technique

key_func (name = "Asif", age = 24)    


## for more check phy notes 
