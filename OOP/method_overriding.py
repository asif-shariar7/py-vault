class Father:
    def skills(self):
        print("I can do Python")

class Son(Father):
    def skills(self):
        print("I can do frontend development")

call = Son()
call.skills()     ## it show the child method, not parent - "I can do frontend development" . because overriding happens (prints only one)