# def task (lst):
#     unique = []

#     for value in lst:
#         if value not in unique:
#             unique.append(value)
  

#     data = {"original_list" : lst,
#             "unique_values" : unique,
#             "count" : len(unique)
#             }

#     return data


# main_list = []
# num = int(input("Enter length of list:  "))

# for i in range(num):
#     main_list.append(int(input(f"Enter the {i} index value: ")))

# result = task(main_list)

# print(result)


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
    s1.add(int(input("Enter value: ")))
print(s1) 

s2 = set()
n2 = int (input("Enter set2 size: "))
for j in range(n2):
    s2.add(int(input("Enter value: ")))
print(s2)

result = task(s1,s2)
print(result)

result2 = task(s1)      ##this function can work even if one of the set is not provided
print(result2)