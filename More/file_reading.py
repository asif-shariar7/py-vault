# reading from file - formula 1

file = open('details.txt', 'r')
content = file.read()
print(content)
file.close()

# formula 2

with open('details.txt', 'r') as f:
    print(f.read())