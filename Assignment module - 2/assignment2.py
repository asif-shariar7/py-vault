##Create a function that accepts two sets as parameters and returns their union, intersection, and difference. Use keyword arguments with default parameter values so the function can work even if one of the sets is not provided by the user. Display the results clearly.

def task(set1 = None, set2 = None):
    if set1 is None:
        set1 = set()    
    if set2 is None:
        set2 = set()  

    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)

    return union, intersection, difference


s1 = set()
n = int(input("Enter set1 size: "))
for i in range(n):
    s1.add(int(input("Enter values: ")))
print("The first set is: ",s1) 

s2 = set()
n2 = int (input("Enter set2 size: "))
for j in range(n2):
    s2.add(int(input("Enter values: ")))
print("The second set is: ",s2)

u,i,d = task(s1,s2)
print("Union of two sets: ",u)
print("Intersection of two sets: ", i)
print("Difference of two sets: ",d)


# u,i,d = task(s1)    ## this function can work even if one of the set is not provided
# print("Union: ",u)
# print("Intersection: ", i)
# print("Difference: ",d)