
guest = {
    "Name" : "Asif",
    "Age"  : 24,
    "favorite_snacks" : "fish"
}

## new value add. No index in dictionary so always add key-value pair in the last

guest["phone_num"] = '0157821981'
print(guest)

## remove the last value
# guest.pop("phone_num")
# print(guest)

##OR
# del guest["favorite_snacks"]
# print(guest)

# guest.clear()
# print(guest)    ## return empty dictionary


##

print(guest.get("Name"))
print (guest["Name"])      ## Same

## updating dictionary
# guest["Name"] = "Nisa"
# print(guest)

## loop in dictionary
for key, value in guest.items():
    print(f"{key} : {value}")

## nested dictionary

person = {
    "person1" : {"Name" : "Asif", "Age" : 24}, 
    "person2" : {"Name" : "Nisa", "Age" : 23}
    }    

print(person["person1"]["Name"])  ## accessing

for key, value in person.items():
    print(f"{key} -> Name = {value['Name']}, Age = {value['Age']}")


## loop for keys

# for i in guest:
#     print(i)    # prints the keys


## dictionary comprehension example

# numbers = list(range(0,6))

# dict = {i:"Even" if i%2 == 0 else "Odd" for i in numbers}
# print(dict)

# for loop for values

# for i in guest.values():
#     print(i)      ## prints values



a = [9,2]
b = [8,7]

result = dict(zip(a,b))   # zip() pairs elements from both lists. Pairs formed: (9, 8) (2, 7)
print(result)     ## output {9: 8, 2: 7}
