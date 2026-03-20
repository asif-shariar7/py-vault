## single inheritance

# class Father:
#     def skills(self):
#         print("I can do frontend development")

# class Son(Father):
#     pass

# inno = Son()
# inno.skills()


## multiple inheritance

# class Father:
#     def skills(self):
#         print("I can do python")

# class Mother:
#     def passion(self):
#         print("I love cooking")

# class Son(Father, Mother):
#     pass

# inno = Son()
# inno.passion()
# inno.skills()

## multilevel inheritance

# class Grandpa:
#     def advice(self):
#         print("Never ignore bugs")

# class Father(Grandpa):
#     def skills (self):
#         print("I can do python")

# class Son (Father):
#     pass

# inno = Son()
# inno.advice()
# inno.skills()


## Hierarchical inheritance

class Mom:
    def passion(self):
        print("Love Cooking")

class Son(Mom):
    pass

class Daughter(Mom):
    pass

inno = Son()
multi = Daughter()
inno.passion()
multi.passion()
