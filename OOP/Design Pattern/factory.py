

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")


class AnimalFactory:
    def check_animal(self, type):
        if type == 'cat':
            return Cat()
        elif type == 'dog':
            return Dog()
        else:
            raise ValueError("Invalid type!!") 

factory = AnimalFactory()

animal1 = factory.check_animal('dog')
animal1.sound()
animal2 = factory.check_animal('cat')
animal2.sound()

# animal2 = factory.check_animal('hwbh')  # error
# animal2.sound()


## How it works ->
# We ask the factory: "dog" or "cat"
# Factory decides which object to create
# You don’t care about class names → only use result