s = {"apple", "banana", "apple", "orange"}

print(s)  ##remove duplicate

s.add("mango")

print(s) ## add new value


## set joining

s2 = {1,2,3}
s.update(s2)
print(s)    ## s update happens

## insert List item in set / join a set with list
l = [5,8,9]
s2.update(l)
print(s2)  # in order

## removing item
s.remove("apple")
print(s)

s.pop()
print(s)

## s.discard(value) works same as remove() but if the value is not present in the set then it shows errors for using remove() but no error shows using discard()

result = s.clear()
print(result)    ## return None
print(s)   ## return empty set / set()

s3 = {"mango", "banana", "nut"}
s4 = {"nut", "orange","pineapple"}

print(s3.union(s4))
print(s3.intersection(s4))
print(s3.difference(s4))

## join a set with tuple

s5 = {4,5,6}
tup = (1,7,9)

s5.update(tup)
print(s5)      ## in order