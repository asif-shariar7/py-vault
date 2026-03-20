##In Python, true method overloading (same method name with different parameters) is not supported like in C++ or Java. But we can achieve similar behavior using default arguments.

# Ex - 1

# class Report:
#     def marks (self, math = None, eng = None):
#         if math is not None and eng is not None:
#             print(f"Math : {math}, English : {eng}")
#         elif math is not None:
#             print(f"Math : {math}")
#         else:
#             print("No marks given")

# result = Report()
# result.marks(78)
# result.marks()
# result.marks(78,89)


# Ex - 2

class Math:
    def add (self, a, b = None):
        if b is None:
            print(a)
        else:
            print(a+b)   
            
show = Math()
show.add(3)
show.add(4,1)    
