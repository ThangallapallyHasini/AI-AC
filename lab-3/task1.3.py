def print_factorials_1_to_5():
    result = 1
    for n in range(1, 6):
        result *= n
        print(f"{n}! = {result}")

# Example usage
print_factorials_1_to_5()