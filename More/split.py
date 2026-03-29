# split() returns a list, but it does not convert other types automatically.


# Ex -> 1

text = "10 20 30"
result = text.split()
print(result)  

# Output - ['10', '20', '30']

## converting to numbers ->

result = list(map(int, text.split()))
print(result)

# Output - [10, 20, 30]