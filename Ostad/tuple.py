tup = ("apple", "banana", "orange","mango")
print(tup)


print(len(tup))

## indexing happens 
print(tup[1])
print(tup[-1])
print(tup[1:3])

## checking
if "apple" in tup:
    print("Yes Present")

## we can not change, remove, insert in tuple but we can do it by converting it into list

l = list(tup)  # tuple convert into list
l.append("pineapple") #insert
l[1] = "nut"   # change
t = tuple(l)   #convert again in tuple. that's how we can do anything in tuple
print(t)   

## unpacking / comparing

# tu = (1,2,5)
# (red,green,blue) = tu
# print(red)  #1
# print(green) #2

## unpacking ex-2

# tu = (1,2,4,5,6)
# (red, *green) = tu
# print(red) # 1
# print(green) #rest all

## unpacking ex-3
tu = (1,2,4,5,6)
(red, *green,blue) = tu
print(red) # 1
print(green) #rest middle all
print(blue) #last one

## joining tuples
tup1 = (1,2,3,9)
tup2 = (1,6,8,4)
result = tup1 + tup2
print(result)   # just joined. no ordering happens or no duplicate vanish happens

# multiply
tup3 = (9,3,1)
tup4 = (8,6)
mul = tup3 * 2
mul2 = tup3 * tup4   # not work!
print(mul)   ## just the tup3 each values comes 2 times 
print(mul2)  ## comes error