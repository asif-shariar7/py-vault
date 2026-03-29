
n = int(input("Enter Number of Student: "))
student_dict = {}

for _ in range(n):
    # Note: We use i when you need the loop index inside the loop. 
    # _ is a convention in Python that means “I don’t care about this variable.” We use _ when we just want to repeat something n times but don’t need the index.

    name = input("Enter Name: ")
    marks = list(map(float, input("Enter marks seperated by space: ").split()))

    student_dict[name] = marks

query_name = input("Enter the name of the student to get average: ")

if query_name in student_dict:
    marks = student_dict[query_name]
    average = sum(marks)/len(marks)
    print(f"{query_name}'s average marks: {average:.2f}")

else:
    print("Student not found")


## Hackerrank style solution 
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     data = input().split()
#     name = data[0]
#     scores = list(map(float, data[1:]))
#     student_marks[name] = scores

# query_name = input()  
# marks = student_marks[query_name]
# average = sum(marks)/len(marks)
# print(f"{average:.2f}")   # here : → start formatting instructions
# #    