## Polymorphism is the ability of a method or function to perform different actions depending on the object that calls it. (One method name, but it can do different things depending on who is using it.)
# Method overriding is true polymorphism in Python
# Poly - multiple, Morphism - form

class Mom:
    def passion(self):
        print("Love Cooking")

class Son(Mom):
    def passion(self):
        print("Love Coding")


def poly (calling):
    calling.passion()

poly(Mom())
poly(Son())    

## Here Both Mom and Son have a method named passion(). Same method name, different behavior.
