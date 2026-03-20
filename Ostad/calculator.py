## simple calculator

def calculator (n1, n2, sign):
    if sign == "+":
        print("Addition result : ",n1 + n2)
    elif sign == "-":
        print("Subtraction result: ",n1 - n2)
    elif sign == "*":
        print("Multiplication result: ",n1 * n2)
    elif sign == "/":
        if n2 != 0:
            print("Division result: ",n1/n2)
        else:
            print("Invalid. Divide by zero not possible")
    elif sign == "%":
        if n2 != 0: 
            print("Remainder is : ", n1 % n2)
        else:
            print("Invalid. Modulo by zero not possible")    
    else:
        print("Invalid operator")

number1 = int(input("Enter your number: "))
number2 = int(input("Enter second number: "))
operator = input("Choose an operator (+,-,*,/,%): ")

calculator(number1, number2, operator)                                    