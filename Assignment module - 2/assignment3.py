## Define a tuple containing mixed data types, unpack its values into separate variables, and compare them with another tuple using comparison operators. Then, explain in code comments the main difference between lists and tuples in Python.

tup = (29,False,"Asif",9.29)
w,x,y,z = tup    ##unpacking tuple 1

tup2 = (7, True, "Shariar", 9.29)
a,b,c,d = tup2     ##unpacking tuple 2

print("Comparing two tuples -> ")
print("tup = tup2: ",tup == tup2)
print("tup != tup2: ",tup != tup2)
print("tup > tup2: ",tup > tup2)
print("tup < tup2: ",tup < tup2)


## The main difference between lists and tuples ->
## List ->  1. List is mutable. we can change, remove, modify list values.
#           2. it uses []

## Tuple ->  1. Tuple is immutable. we can not change, remove, modify tuple values
#            2. it uses ()
