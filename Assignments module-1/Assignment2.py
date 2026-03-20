## Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sign = input("Choose a operator in between (+,-,*,/) : ")

if sign == '+':
    print("After adding two numbers the result is: ",(number1+number2))

elif sign == '-':
    print("After subtracting two numbers the result is: ",(number1-number2))

elif sign == '*':
    print("After multiplying two numbers the result is: ",(number1*number2))

elif sign == '/':
    if number2 != 0:
        print("After dividing two numbers the result is: ",(number1/number2)) 
    else:
        print("Can not divided by zero")
else:
    print("Invalid Choice! Choose Correct Operator.")               