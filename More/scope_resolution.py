# x = "Global"   # global variable

# def fun():
#     x = "Local"   # local variable
#     print(x)

# fun()
# print(x)

# ---

x = 20  # global variable

def outer():
    x = 25     # enclosing variable
    def inner():
        x = 10  # local variable
        print(x)  # 10 inner() call e
    inner()
    print(x)  #25 outer() call e
outer()
print(x)   # 20 - because global 

## keyword

n = "Global"

def change():
    global n
    n = "Local"

change()  # Output - Local
print(n)


#
def Outer():
    x = "Enclosing"
    def Inner():
        # nonlocal x
        x = "Local"
        print(x)   # output - local
    Inner()
    print(x)  # output - local , nonlocal use na korle output - Enclosing

Outer()     