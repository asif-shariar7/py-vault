
# class A:
#     def show(self):
#         print("A")

# class B:
#     def show(self):
#         print("B")

# class C(A,B):
#     def show(self):
#         print("C")

# obj = C()
# obj.show()    # output -  C. not go to A from C because no super()


# print(C.__mro__)    # for checking MRO
# help(C)

print("\n")
# OR - print()


# class A:
#     def show(self):
#         print("A")

# class B:
#     def show(self):
#         super().show()
#         print("B")

# class C(A,B):
#     def show(self):
#         super().show()
#         print("C")

# obj = C()
# obj.show()  # Output - A C
# # A.show() does NOT call super(), so the chain stops here. 
# print(C.__mro__)


## BUT 
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(B,A):       # not C(A,B)
    def show(self):
        super().show()
        print("C")

obj = C()
obj.show()  # Output - A B C

### More study and practice needed