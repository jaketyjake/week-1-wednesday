import calculator

number1 = int(input("What is the first number?"))
number2 = int(input("What is the second number?"))
operand = str(input("Do you want to multiply, divide, subtract, or add? '*', '/', '-', '+'?"))
result = 0

if operand == '*':
    result = calculator.multiply(number1,number2)
    print(f"{number1} times {number2} is {result}")
elif operand == '/':
    result = calculator.divide(number1,number2)
    print(f"{number1} divided by {number2} is {result}") 
elif operand == '-':
    result = calculator.subtract(number1,number2)
    print(f"{number1} minus {number2} is {result}")
elif operand == '+':
    result = calculator.add(number1,number2)
    print(f"{number1} plus {number2} is {result}")
