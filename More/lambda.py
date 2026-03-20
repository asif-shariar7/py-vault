# anonymous function or unnamed - Use no print(). it only returns. it make small the function

square = lambda x : x*x
print(square(2))


## sort the nested list according the numbers -
li = [['Asif',198], ['Nisa',197]]   # indexing - Asif = 0, 198 = 1

result = sorted(li, key = lambda x : x[1])
print(result)


# map()
# map(ki korte chacchi, kar upor e korte chacchi)

lis = [1,2,3,4]
show = list(map(lambda x : x*x, lis))
print(show)

# filter()

new = list(map(lambda x : x%2 == 0,lis))
print(new)    # [False, True, False, True]

new = list(filter(lambda x : x%2 == 0,lis))
print(new) 

# reduce()

import functools

add = functools.reduce(lambda x, y: x + y, lis)    # functools.reduce() always passes two values at a time to the lambda
print(add)
