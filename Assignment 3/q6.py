def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)

print("Addition:", calculate(7, 5, add))
print("Subtraction:", calculate(7, 5, subtract))
print("Multiplication:", calculate(7, 5, multiply))
print("Division:", calculate(7, 5, divide))

print("Division by zero test:", calculate(10, 0, divide))
