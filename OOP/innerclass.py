## Accessing Inner Class from the Outside

class Outer:
    def __init__(self, name):
        self.name = name

    class Inner:
        def __init__(self, name):
            self.name = name

        def show(self):
            print(f"Hello! I am {self.name}")

outerObj = Outer("Outer")
print(outerObj.name)    # Outer
innerObj = outerObj.Inner("Inner")
innerObj.show()   # Hello! I am Inner