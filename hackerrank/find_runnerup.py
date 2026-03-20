n = int(input())
scores = list(map(int, input().split()))  ## Here ->

# input() - Reads a line from the user as a string.
# Example: if the user types 2 3 6 6 5, then input() gives the string:
# "2 3 6 6 5"
# .split()
# Splits the string into a list of smaller strings, using space as the default separator.
# Example:
# "2 3 6 6 5".split()  # → ['2', '3', '6', '6', '5']
# map(int, ...)
# map applies a function (here int) to each item of a list (or iterable).
# So it converts each string into an integer:
# map(int, ['2', '3', '6', '6', '5'])  # → [2, 3, 6, 6, 5] (as a map object)

# print(scores)
# result = list(set(scores))
# print(result)
# print(result[-2])


## ??    
result = list(set(scores))
result.sort()      # set() removes duplicates but does NOT keep order. so we need to use sort()
print(result[-2])