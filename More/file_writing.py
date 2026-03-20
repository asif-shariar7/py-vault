## writing in a file. first write then read
# with open('details.txt', 'a') as f:
#     f.write("Hello")

# with open('details.txt', 'r') as f:
#     print(f.read())


# ---
with open('details.txt','w') as f:
    f.write("\nHello! I am testing write function\n")

# -- list write kora -->

l = ['I love Python\n', 'I am in basic stage']

with open ('details.txt', 'a') as file:
    file.writelines   