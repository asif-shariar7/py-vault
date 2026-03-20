## Create three classes Animal, Mammal, and Dog where Animal has a method eat(), Mammal inherits from Animal and has a method walk(), and Dog inherits from Mammal and has a method bark(). Create an object of Dog and demonstrate all three methods. Also, create a class Calculator with an add() method that can take either two or three parameters, and then create a subclass AdvancedCalculator that overrides the add() method to add any number of parameters using variable-length arguments. Demonstrate both functionalities.


# part 1
class Animal:
    def eat(self):
       print("Animal is eating")

class Mammal(Animal):
    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking")

obj = Dog()
obj.eat()
obj.walk()
obj.bark()


# part 2
class Calculator:
    def add (self, a , b , c = None):
        if c is not None:
            return a + b + c
        else:
            return a + b
        
class AdvancedCalculator(Calculator):
    def add (self, *arg):
        return sum(arg)        
    
calc = Calculator()
print("add two number : ", calc.add(5,6))
print("add three number : ", calc.add(5,6,7))


advcalc = AdvancedCalculator()
print("add two number : ", advcalc.add(5,8))
print("add four number : ", advcalc.add(5,6,7,9))
print("add six number : ", advcalc.add(5,6,7,9,1,3))