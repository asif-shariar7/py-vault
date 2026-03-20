# syntax - map(function, iterable). 
# function → what you want to apply (e.g., int, str, len). iterable → list, tuple, etc.


l = ["2", "3", "5"]

result = map(int, l)

print(list(result))   #Output: [2, 3, 5] . map() converted all strings to integers.


# if user types - 2 3 6 6 5

num = int(input())
arr = list(map(int, input().split()))
print(arr)     ## Here ->

# Input:
# 5
# 2 3 6 6 5

# Step-by-step:
# n = int(input())
# → n = 5
# input().split()
# "2 3 6 6 5" → ['2', '3', '6', '6', '5']
# map(int, ...)
# ['2','3','6','6','5'] → 2 3 6 6 5
# list()
# [2, 3, 6, 6, 5]

# Output:
# [2, 3, 6, 6, 5]