def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operator"

# Example usage:
result = calculator(5, 3, '+')
print(result)  # Output: 8
