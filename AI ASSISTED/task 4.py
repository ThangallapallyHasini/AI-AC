def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

# Example usage
x = 10
y = 5
print("Add:", calculator(x, y, '+'))
print("Subtract:", calculator(x, y, '-'))
print("Multiply:", calculator(x, y, '*'))
print("Divide:", calculator(x, y, '/'))