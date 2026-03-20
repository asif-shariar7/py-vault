import os

print(os.path.abspath('details.txt'))  #path dekhai (full file location)
print(os.path.getsize('details.txt'))  # size in bytes

if os.path.exists('details.txt'):
    print("File Exists")
else:
    print("File is not exists")    