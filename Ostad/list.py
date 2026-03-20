# Story Outline:
# Once upon a time in the magical land of Pylandia, a bunch of data structures threw a party.

# Lists were the cool kids who loved to collect everything: snacks, jokes, and even exes.

# Dictionaries were the classy ones, always coming with pairs — name cards and phone numbers!

# Functions were the organizers of the party. They did all the work, especially Chef Function, who always asked for parameters like "ingredient" or "dish_type".

# Sometimes, Chef Function would get moody if you didn't pass the right arguments — unless he had default values ready, like pizza 🍕!

# They all had to go home at midnight, so they shouted return "BYE" and vanished!

# The list guy walks in with: ["Chips", "Soda", "Cake"]


# l = ["chips", "soda", "cake"]
# l.append("apple")   #always add items at the last
# print("After adding the new list is ",l)

# l.remove("soda")
# print("After removing item new list is: ",l)

## ascending / words thakle alphabet onujayi sort hbe
# l2 = [2,4,51,9]
# l2.sort()
# print(l2)

## descending

# l = [2,9,1,5,13]
# l.sort(reverse=True)
# print(l)


## indexding

# l = [3,4,1,6,7]
# print(l[-1])  ##7 (minus indexing)
# print(l[0])   ##3

# ## set in index 1 of l - 99
# l[1] = 99
# print(l)
# print(len(l))   ## length

##
# l = [8,9,0,1,3]
# l.insert(2,11)  ## insert 11 in index 2
# print(l)

# del l[3]  ## delete index 3
# print(l)

# l.pop()
# print(l)   ## last item delete

# l.clear()
# print(l)  ## return empty list because of clear


## nested list 
# l = [[2,4], [6,8],[5,6]]

# for i in l:
#     for j in i:
#         print(j)

l1 = [8,9]
l2 = [6,2]
print(l1+l2)   ## joining list