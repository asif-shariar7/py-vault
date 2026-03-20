## 4 types - 1.No input + no return 2.Input + No return 3. No input + return 4. input + return

# arbitrary arguments

def addition(*args):
    print(args)     # return tuple - (2,3,4,1)
    print(args[0]+args[1]+args[2]+args[3])

addition(2,3,4,1)

#arbitrary keyword arguments

def multiplication(**kwargs):
    print(kwargs)  # return dictionary - {'a1': 3, 'a2': 4}
    print(f"{kwargs['a1'] * kwargs['a2']}")

multiplication(a1 = 3, a2 = 4)