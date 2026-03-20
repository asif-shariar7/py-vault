##Write a Python program that takes a list of numbers as input, removes duplicates using a suitable list method, and returns a dictionary containing the original list, the unique values, and their count. Use a function with parameters and a return statement to perform this task.

def task (lst):
    unique = []

    for value in lst:
        if value not in unique:
            unique.append(value)
  

    data = {"original_list" : lst,
            "unique_values" : unique,
            "count" : len(unique)
            }

    return data


main_list = []
num = int(input("Enter length of list:  "))

for i in range(num):
    main_list.append(int(input(f"Enter the {i} index value: ")))

result = task(main_list)

print(result)