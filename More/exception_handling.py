try:
    # 1
    # with open('d.txt','r') as f:
    #     print(f.read())
    with open('details.txt','r') as f:
        print(f.read())

    # 2
    l = [1,3,5]
    # print(l[100])  
    print(l[2])

    # 3
    # print(10/0)  
    print(10/10)

    # 4
    # n = int('abc')  # -> this not possible. so value error

    # 5
    # x = abc    # Unknown error

except FileNotFoundError:
    print("File doesn't exists")

except IndexError:
    print("Invalid index")

except ZeroDivisionError:
    print("Divide by zero is not possible")

except ValueError:
    print("Not possible")

except Exception as e:       # for unknown errors
    print("Error happens!", e)    

# else - goes to else if try success 

else:
    print("Code executed successfully!!")

finally:
    print("Always runs if there exists error or not")  


# Manually trigger a exception (custom error). suppose, someone upload .csv file instead of .txt file

def check(filename):
    if not filename.endswith('.txt'):
#endswith() is a Python string method used to check whether a string ends with a specific substring.
        raise FileNotFoundError("Only .txt files are allowed")
    print("Valid")

# custom error handling
try:
    check('test.csv') 

except Exception as e:
    print(e)           