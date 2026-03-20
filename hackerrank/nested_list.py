## nested list user input


n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input("Enter Name: ")
    grade = float(input("Enter Grade: "))
    students.append([name,grade])


print(students)

## now prints second lowest grade

# Extract all grades. list comprehension -
grades = [g for n, g in students]

## ------
## Or ->
# grades = []
# for s in students:
#     grades.append(s[1])
#Why s[1]?
# If the list is:
# students = [
#     ['Alice', 50],
#     ['Bob', 70],
#     ['Charlie', 60]
# ]
# Each element looks like:
# ['Alice', 50]
#    0      1

# s[0] → name
# s[1] → grade
# So the loop extracts the grades.
# Result:
# grades = [50, 70, 60]
# print(grades)

## ------
result = sorted(set(grades))
# print(result)
second_lowest = result[1]   # second lowest grade


# Now Find students with second lowest grade

names = []

for name,grade in students:
    if grade == second_lowest:
        names.append(name)       
        
# If multiple students have the same grade: names = ['Charlie','David']. then sort names alphabetically

names.sort()
for name in names:
    print(name)    # Print each name