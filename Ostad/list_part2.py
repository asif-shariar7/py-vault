## input list values from user input

l = []
n = int(input("Enter the length of list: "))

for i in range(n):
    l.append(int(input(f"Enter {i} index value: ")))

print(l)

## remove duplicates
unique = []

for value in l:
    if value not in unique:
        unique.append(value)

print(unique)  

## store in dictionary

data = {"original_list" : l,
         "unique_value" : unique,
         "count" : len(unique)
        
        }
print(data)